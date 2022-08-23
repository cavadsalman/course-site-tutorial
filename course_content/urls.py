from django.urls import path

from . import views

urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('create-course/', views.create_course, name='create-course'),
    path('create-tag/', views.create_tag, name='create-tag'),
    path('create-lesson/<int:pk>/', views.create_lesson, name='create-lesson'),
    path('delete-lesson<int:pk>/', views.delete_lesson, name='delete-lesson'),
    path('update-lesson<int:pk>/', views.update_lesson, name='update-lesson'),
    path('course-detail/<int:pk>/', views.course_detail, name='course-detail'),
    path('lesson-detail/<int:pk>/', views.lesson_detail, name='lesson-detail')
]