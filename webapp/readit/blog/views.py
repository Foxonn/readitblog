from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category

from readitcomments.models import Comment
from readitcomments.forms import CommentForm
from readitcomments.services import exist_user
from task import task_notify_admin, task_notify_user, task_notify_new_responded


def blog_dispatcher(request, match):
    if match and Post.objects.filter(url=match).first():
        context = {}

        post = post_detail(request, match)

        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                user = exist_user(form.cleaned_data['name'], form.cleaned_data['email'])
                post = get_object_or_404(Post, id=form.cleaned_data['post'])

                comment = Comment(message=form.cleaned_data['message'], user=user, post=post)
                comment.save()

                if form.cleaned_data['replys']:
                    parent_comment = get_object_or_404(Comment, id=form.cleaned_data['replys'])
                    parent_comment.comments_replys.add(comment)
                    parent_comment.save()

                comment_link = '{}#comment_{}'.format(post.get_absolute_url(), comment.id)

                task_notify_admin.spool({'user_name': user.name, 'comment_link': comment_link})
                task_notify_user.spool({'user_email': user.email, 'comment_link': comment_link})

                return redirect(post)
        else:
            form = CommentForm()

        context.update({'form': form})
        context.update(post)

        return render(request, 'blog/post/post_detail.html', context)

    if match and Category.objects.filter(url=match).first():
        context = post_list(request, match)
        return render(request, 'blog/post/post_list.html', context)

    return render(request, 'blog/404.html', status=404)


def post_list(request, match=None):
    if not match:
        posts = get_list_or_404(Post.objects.all())
    else:
        posts = Post.objects.filter(category__url=match)

    if not posts:
        return None

    paginator = Paginator(posts, 9, 3)

    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {'page_obj': page_obj, 'paginator': paginator}

    if match:
        return context

    return render(request, 'blog/post/post_list.html', context)


def post_detail(request, url):
    post = Post.objects.get(url=url)

    return {'post': post}
