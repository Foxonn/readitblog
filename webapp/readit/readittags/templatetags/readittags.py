from django import template
from django.urls import reverse_lazy
from readittags.models import Tag

register = template.Library()


@register.inclusion_tag('readittags/cloud_tags.html')
def tags_cloud() -> list:
    tags = Tag.objects.all().only('name', 'slug')

    if not tags:
        pass

    return {'tags': [{'name': tag.name, 'url': reverse_lazy("tag:tag_posts", args=[tag.slug])} for tag in tags]}
