from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import (
    TagForm, 
    CourseForm, 
    LessonForm, 
    CourseSearchForm,
    CoursePriceForm
)
from .models import Course, Tag, Lesson
from django.db.models import Count

# Create your views here.

@login_required(login_url='login-student')
def course_list(request):
    courses = Course.objects.all()
    tags = Tag.objects.all()
    course_search_form = CourseSearchForm()
    course_price_form = CoursePriceForm()
    get_data = request.GET
    filter_type = get_data.get('filter_type')
    if filter_type == 'search':
        course_search_form = CourseSearchForm(get_data)
        if course_search_form.is_valid():
            cd = course_search_form.cleaned_data
            courses = courses.filter(title__icontains=cd.get('title'))
    elif filter_type == 'price':
        course_price_form = CoursePriceForm(get_data)
        if course_price_form.is_valid():
            cd = course_price_form.cleaned_data
            courses = courses.filter(price__range=(cd.get('min_value'), cd.get('max_value')))
    elif filter_type == 'tag':
        courses = courses.filter(tag = get_data.get('tag_id'))
    return render(request, 'course-list.html', context={
        'courses': courses,
        'course_search_form': course_search_form,
        'course_price_form': course_price_form,
        'tags': tags
    })

@login_required(login_url='login-teacher')
def create_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-course')

    courses = request.user.teacher.course_set.all().annotate(lesson_count=Count('lesson'))

    return render(request, 'create-course.html', context = {
        'form': form,
        'courses': courses
    })


@login_required(login_url='login-teacher')
def create_lesson(request, pk):
    lessons = Lesson.objects.filter(course=pk)
    form = LessonForm(initial={'course': pk})
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-lesson', pk=pk)
    return render(request, 'create-lesson.html', context={
        'form': form,
        'lessons': lessons
    })

@login_required(login_url='login-teacher')
def delete_lesson(request, pk):
    object = get_object_or_404(Lesson, pk=pk)
    course_pk = object.course.pk
    object.delete()
    return redirect('create-lesson', pk=course_pk)

@login_required(login_url='login-teacher')
def update_lesson(request, pk):
    object = get_object_or_404(Lesson, pk=pk)
    course_pk = object.course.pk
    form = LessonForm(instance=object)
    if request.method == 'POST':
        form = LessonForm(instance=object, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-lesson', pk=course_pk)
    return render(request, 'update-lesson.html', context={
        'form': form,
    })

@login_required(login_url='login-teacher')
def create_tag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-tag')

    tags = Tag.objects.all()
    return render(request, 'create-tag.html', context={
        'form': form,
        'tags': tags
    })


def course_detail(request, pk):
    object = get_object_or_404(Course, pk=pk)
    return render(request, 'course-detail.html', context={
        'course': object
    })

def lesson_detail(request, pk):
    object = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lesson-detail.html', context={
        'lesson': object
    })


