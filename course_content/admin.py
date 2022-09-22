from django.contrib import admin
from .models import Tag, Course, Lesson
# Register your models here.

admin.site.register(Tag)
admin.site.register(Lesson)

@admin.action(description='Deaktiv Et')
def deactivate(modeladmin, request, queryset):
    queryset.update(active=False)
    
@admin.action(description='Aktiv Et')
def activate(modeladmin, request, queryset):
    queryset.update(active=True)
    
class LessonInline(admin.TabularInline):
    model = Lesson
    readonly_fields = ('view_count',)
    extra = 1
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # fields = ('teacher', 'title', 'description',
    #           'tag', 'rate', 'price', 'image', 'active', ('updated', 'created'))
    fieldsets = (
        ('Melumat', {
            'fields': ('teacher', 'title', 'description'),
            'classes': ('show',)
        }),
        ('Detallar', {
            'fields': ('tag', 'rate', 'view_count', 'price', ('image_tag', 'image'), 'active', ('updated', 'created'))
        })
    )
    readonly_fields = ('image_tag', 'updated', 'created', 'view_count')
    list_display = ('title', 'teacher', 'price', 'active', 'created', 'course_link', 'lesson_count')
    list_display_links = ('title',)
    list_filter = ('teacher', 'tag', 'updated')
    list_editable = ('price',)
    search_fields = ('title', 'description', '=teacher__user__first_name', 'teacher__user__last_name')
    actions = (activate, deactivate)
    inlines = (LessonInline,)