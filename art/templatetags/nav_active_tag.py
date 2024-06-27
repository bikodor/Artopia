from django import template
from django.urls import reverse, NoReverseMatch



register = template.Library()

@register.simple_tag(takes_context=True)
def nav_active(context, url_name, css_class='active'):
    try:
        path = reverse(url_name)
    except NoReverseMatch:
        path = url_name
    if context['request'].path == path:
        return css_class
    return ''

