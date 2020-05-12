from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseNotFound, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post


def tagspostlist(request, slug):
    if not slug:
        return render(request, 'blog/404.html', status=404)

    posts = Post.objects.filter(tags__slug=slug)

    paginator = Paginator(posts, 9, 3)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {'page_obj': page_obj, 'paginator': paginator}

    return render(request, 'blog/post/post_list.html', context)
