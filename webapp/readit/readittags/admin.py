from django.contrib import admin
from django.utils.translation import gettext_lazy
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        verbose_name = gettext_lazy('tags_verbose_name')
        verbose_name_plural = gettext_lazy('tags_verbose_name_plural')
