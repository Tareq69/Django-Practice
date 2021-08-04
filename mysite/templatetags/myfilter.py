from django import template

register = template.Library()

def my_filter(value):
    return value + 100

register.filter('custom_filter', my_filter)
