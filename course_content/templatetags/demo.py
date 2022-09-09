from django import template
from django.utils.safestring import mark_safe
from course_content.models import Tag

register = template.Library()
eq = {'ə': 'e', "ü": "u", 'ö': 'o', 'ğ': 'g', 'ç': 'c', 'ğ': 'g' , 'ş': 's'}
@register.filter
def make_ascii(text):
    result = ''
    for char in text:
        if char in eq:
            result += eq.get(char)
        else:
            result += char
            
    return result


@register.simple_tag
def cut_text(text, length=30):
    if len(text) > length:
        return text[:length-3] + '...'
    else:
        return mark_safe(text)
    
    
@register.inclusion_tag('components/tags.html')
def tag_list(a_class):
    tags = Tag.objects.all()
    return {
        'a_class': a_class,
        'tags': tags
    }
    
