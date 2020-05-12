from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/tags/categories_menu.html')
def categories_menu() -> list:
    categories = Category.objects.all().only('title')

    if not categories:
        raise ValueError('Empty value `categories`.')

    return {'categories': [{'title': category.title, 'url': category.get_absolute_url} for
                               category in categories]}


