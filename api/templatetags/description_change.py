from django.template import Library
from api.models import Product, Redikt

register = Library()

@register.filter()
def description_change(request, obj: Product) -> bool:
    data = {
        'uz': obj.description_uz,
        'ru': obj.description_ru,
        'en': obj.description_en
    }
    lang = request.path.split('/')[1]

    return data[lang]