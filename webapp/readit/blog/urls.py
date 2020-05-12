from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='home'),
    re_path(r'^(?P<match>.+)/$', views.blog_dispatcher, name='blog_dispatcher'),
]