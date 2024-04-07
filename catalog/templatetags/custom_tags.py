from django import template

register = template.Library()


@register.filter()
def catalog_media(data):
    if data:
        return f'/media/{data}'
    return '#'
