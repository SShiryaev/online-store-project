from django.conf import settings
from django.core.cache import cache

from models import Category


def get_category_from_cache():
    # если кеш (редис) включен, то кешируем категории (типы СЗР) из БД

    if settings.CACHE_ENABLED:
        key = 'categories_list'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
        else:
            categories = Category.objects.all()

        return categories
