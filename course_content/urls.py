from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('create-course/', views.create_course, name='create-course'),
    path('create-tag/', views.CreateTagView.as_view(), name='create-tag'),
    path('lesson-list/<int:course_pk>/', views.LessonListView.as_view(), name='lesson-list'),
    path('create-lesson/<int:pk>/', views.create_lesson, name='create-lesson'),
    path('delete-lesson<int:pk>/', views.delete_lesson, name='delete-lesson'),
    path('update-lesson<int:pk>/', views.update_lesson, name='update-lesson'),
    path('course-detail/<int:pk>/', views.CourseDeatilView.as_view(), name='course-detail'),
    path('lesson-detail/<int:pk>/', views.lesson_detail, name='lesson-detail'),
    path('tag-detail/<int:pk>/<str:info>/', views.TagDetailView.as_view(), name='tag-detail'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about')
]