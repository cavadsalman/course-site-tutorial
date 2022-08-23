from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm, TeacherForm
from django.contrib.auth.models import User
from .models import Teacher, Student
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_student(request):
    form = LoginForm()
    return render(request, 'login.html', context={
        'form': form,
        'user_type': 'Student'
    })

def register_student(request):
    form = RegisterForm()
    return render(request, 'register.html', context={
        'form': form,
        'user_type': 'Student'
    })

def login_teacher(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_info, password = cd.get('user_info'), cd.get('password')
            if '@' in user_info:
                user = User.objects.filter(email=user_info).first()
            else:
                user = User.objects.filter(username=user_info).first()
            if user and user.check_password(password):
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('course-list')

            
    return render(request, 'login.html', context={
        'form': form,
        'user_type': 'Teacher'
    })

    
def register_teacher(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username = cd.get('username'),
                first_name = cd.get('first_name'),
                last_name = cd.get('last_name'),
                email = cd.get('email'),
                password = cd.get('password'),
            )
            teacher = Teacher.objects.create(user = user)
            return redirect('login-teacher')

    return render(request, 'register.html', context={
        'form': form,
        'user_type': 'Teacher'
    })

def logout_view(request):
    logout(request)
    return redirect('course-list')


def teacher_profile(request, pk):
    teacher = get_object_or_404(Teacher, user=pk)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(instance=teacher, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.get_full_path())
    return render(request, 'teacher-profile.html', context={
        'form': form,
        'teacher': teacher
    })