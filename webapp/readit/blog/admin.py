from django.contrib import admin
from .models import Post, Category
from django import forms
from simple_history.admin import SimpleHistoryAdmin
from django.db import models
# from ckeditor.widgets import CKEditorWidget
from ckeditor5.widgets import CKEditor5Widget
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'slug', 'created', 'updated', 'parent', 'available',)
    search_fields = ('title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('parent',)
    list_editable = ['available']
    fields = (('title', 'slug', 'cat_link',), 'available', 'parent')
    readonly_fields = ('cat_link',)

    def cat_link(self, obj):
        if obj.url:
            url = reverse_lazy('blog:blog_dispatcher', args=[obj.url])
            return mark_safe(f'<a href="{url}" target="_blank">{url}</a>')


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(SimpleHistoryAdmin):
    form = PostAdminForm

    fields = (('title', 'slug', 'post_link',), 'description', 'short_description', 'image', 'images', 'category', 'tags', 'available',)
    list_display = ('title', 'short_description', 'category', 'author', 'available',)
    list_filter = ('author', 'available',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('created',)
    autocomplete_fields = ('tags', 'category',)
    list_editable = ['available', ]
    readonly_fields = ('post_link',)

    def post_link(self, obj):
        if obj.url:
            url = reverse_lazy('blog:blog_dispatcher', args=[obj.url])
            return mark_safe(f'<a href="{url}" target="_blank">{url}</a>')
