from django.shortcuts import render, get_object_or_404
from blog.models import Post


def comment_thanks(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'readitcomments/comment_thanks.html', {'post_link': post.get_absolute_url()})
