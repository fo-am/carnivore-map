from django import template
from django.template.defaultfilters import stringfilter

def escapenewline(value):
    """
    Adds a slash before any newline. Useful for loading a multi-line html chunk
    into a Javascript variable.
    """
    return value.replace('\r\n', '<br>')
escapenewline.is_safe = True
escapenewline = stringfilter(escapenewline)

register = template.Library()
register.filter('escapenewline', escapenewline)
