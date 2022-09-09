from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def general_cut_text(text, length=30):
    if len(text) > length:
        return text[:length-3] + '...'
    else:
        return mark_safe(text)
    