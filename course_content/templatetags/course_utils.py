from django import template

register = template.Library()

@register.filter
def create_range(number, total=0):
    return range(abs(total-number))