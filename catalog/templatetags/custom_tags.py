from django import template

register = template.Library()


@register.filter()
def url_media(data):
    if data:
        return f'/media/{data}'
    return '#'


@register.filter()
def is_moderator(user):
    return user.groups.filter(name='moderator').exists()
