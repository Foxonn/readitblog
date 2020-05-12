from django.urls import path
from . import views

app_name = 'tag'

urlpatterns = [
    path('<slug:slug>/', views.tagspostlist, name='tag_posts'),
]