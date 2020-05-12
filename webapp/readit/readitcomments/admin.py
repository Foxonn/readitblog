from django.contrib import admin
from .models import User, Comment


# Register your models here.
@admin.register(User)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email'
    ]
    list_display_links = ['name']
    readonly_fields = ('name', 'email')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['user', 'replys', 'message', 'published']
    list_display = [
        'user',
        'created',
        'published',
    ]
    list_editable = ['published']
    list_display_links = ['user']
    readonly_fields = ('user', 'replys')
