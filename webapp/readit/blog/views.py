from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category


def blog_dispatcher(request, match):
    if match and Post.objects.filter(url=match).first():
        post = get_object_or_404(Post, url=match)
        return render(request, 'blog/post/post_detail.html', context={'post': post, 'request': request})

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
