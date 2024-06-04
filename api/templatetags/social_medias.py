from django import template
from api.models import Social_media

register = template.Library()

@register.simple_tag
def social_media_icons():
    social_medias = Social_media.objects.all()
    return social_medias
