from django import template

register = template.Library()


@register.filter()
def catalog_media_material(data):
    if data:
        return f'/media/{data}'
    return '#'
