from django.urls import path
from . import views

app_name = 'ckeditor5'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
]
