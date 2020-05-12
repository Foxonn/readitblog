from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def compile_breadcrumbs(obj) -> list:
    """Сборка хлебных крошек"""
    _b = [{'title': obj.title, 'url': obj.get_absolute_url()}]

    if obj.model_field_exists('category'):
        obj = obj.category
        _b.append({'title': obj.title, 'url': obj.get_absolute_url()})

    while obj.parent:
        obj = obj.parent
        _b.append({'title': obj.title, 'url': obj.get_absolute_url()})

    return _b[::-1]


def compile_url(obj) -> list:
    """Сборка урла страница, подкатегории, категория"""
    _p = [obj.slug]

    if obj.model_field_exists('category'):
        obj = obj.category
        _p.append(obj.slug)

    if obj.model_field_exists('parent'):
        while obj.parent:
            obj = obj.parent
            _p.append(obj.slug)

    return '/'.join(_p[::-1])


def not_self_i_me_parent(obj) -> Exception:
    """Категория неможет быть сама себе родителем"""
    if obj.parent and obj.parent.id == obj.id:
        raise ValidationError({'parent': gettext_lazy('A category cannot refer to self.')})

    return None


def wrong_hierarchy(obj, model) -> Exception:
    """Дочерние категории немогут быть родителями предков"""
    if obj.parent:
        _parent = obj.parent

        while _parent:
            category = model.objects.get(id=_parent.id)

            if category.parent:
                if category.parent.id == obj.id:
                    raise ValidationError({'parent': gettext_lazy('The wrong hierarchy.')})
                else:
                    _parent = category.parent
            else:
                break
    return None
