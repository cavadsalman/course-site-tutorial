from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='teacher_photos/', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField('course_content.Course')

    def __str__(self):
        return self.user.first_name