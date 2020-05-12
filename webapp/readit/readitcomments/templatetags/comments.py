from django import template
from readitcomments.forms import CommentForm
from readitcomments.models import Comment

register = template.Library()


@register.inclusion_tag('readitcomments/comments.html')
def comments(post):
    if not post:
        raise ValueError("Input args `post` undefined.")

    comments = Comment.objects.prefetch_related('comments_replys').filter(post__id=post, published=True, replys=None)
    count = Comment.objects.filter(post__id=post, published=True).count()

    return {'comments': comments, 'count': count}


@register.inclusion_tag('readitcomments/form_comments.html')
def form_comments(form, post):
    if not form or not post:
        raise ValueError("Input args `form`, `post` undefined.")

    return {'form': form, 'post': post}
