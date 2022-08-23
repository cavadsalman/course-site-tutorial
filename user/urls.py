from django.urls import path
from . import views

urlpatterns = [
    path('login/student/', views.login_student, name='login-student'),
    path('login/teacher/', views.login_teacher, name='login-teacher'),
    path('register/student/', views.register_student, name='register-student'),
    path('register/teacher/', views.register_teacher, name='register-teacher'),
    path('profile/teacher/<int:pk>/', views.teacher_profile, name='teacher-profile'),
    path('logout/', views.logout_view, name='logout')
]