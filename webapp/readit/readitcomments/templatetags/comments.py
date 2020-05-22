from django import template
from django.shortcuts import get_object_or_404
from blog.models import Post
from readitcomments.forms import CommentForm
from readitcomments.models import Comment
from readitcomments.services import exist_user
from readitcomments.tasks import task_notify_admin, task_notify_user

register = template.Library()


@register.inclusion_tag('readitcomments/comments.html')
def comments(post_id):
    comments = Comment.objects.prefetch_related('comments_replys').filter(post__id=post_id, published=True, replys=None)
    count = Comment.objects.filter(post__id=post_id, published=True).count()

    return {'comments': comments, 'count': count}


@register.inclusion_tag('readitcomments/form_comments.html')
def form_comments(request, post_id):
    form = None

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            user = exist_user(form.cleaned_data['name'], form.cleaned_data['email'])

            post = get_object_or_404(Post, id=post_id)

            comment = Comment(message=form.cleaned_data['message'], user=user, post=post)
            comment.save()

            if form.cleaned_data['replys']:
                parent_comment = get_object_or_404(Comment, id=form.cleaned_data['replys'])
                parent_comment.comments_replys.add(comment)
                parent_comment.save()

            comment_link = '{}#comment_{}'.format(post.get_absolute_url(), comment.id)

            task_notify_admin.delay({'user_name': user.name, 'comment_link': comment_link})
            task_notify_user.delay({'user_email': user.email, 'comment_link': comment_link})

            form = CommentForm()
    else:
        form = CommentForm()

    return {'form': form, 'post_id': post_id}
