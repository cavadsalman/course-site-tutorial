from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.utils.translation import get_language

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("tag-detail", kwargs={"pk": self.pk, "info": "info"})
    



class Course(models.Model):
    teacher = models.ForeignKey('user.Teacher', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, verbose_name='Basliq')
    description = RichTextField()
    rate = models.IntegerField()
    tag = models.ManyToManyField(Tag)
    view_count = models.IntegerField(default=0)
    price = models.FloatField()
    image = models.ImageField(upload_to='course_image/')
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Dəyişildi')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Yaradıldı')
    
    def __str__(self):
        return self.title.upper()
    
    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'
        
    def lesson_count(self):
        return self.lesson_set.count()
    
    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})
    
    def image_tag(self):
        return format_html(f'<img src="{self.image.url}" width="200"/>')
    image_tag.short_description = 'Movcud Sekil'
    
    @admin.display
    def course_link(self):
        return format_html(f'<a href="{self.get_absolute_url()}" target="_blank">Kecid</a>')
    course_link.short_description = 'Kecid Linki'
    
    

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    title_az = models.CharField(max_length=100, null=True, blank=True)
    title_ru = models.CharField(max_length=100, null=True, blank=True)
    video = models.CharField(max_length=300)
    view_count = models.IntegerField(default=0)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def lang_title(self):
        if get_language() == 'az' and self.title_az:
            return self.title_az
        elif get_language() == 'ru' and self.title_ru:
            return self.title_ru
        else:
            return self.title
        
        

    def __str__(self):
        return self.title