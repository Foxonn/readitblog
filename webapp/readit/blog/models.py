from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy
from readittags.models import Tag
from django.utils.text import slugify
from simple_history import register
from django.urls import reverse_lazy
from blog.services import models as smodel
import os


class BlogModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=gettext_lazy('title'))
    slug = models.CharField(max_length=200, verbose_name=gettext_lazy('slug'), unique=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=gettext_lazy('updated'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=gettext_lazy('created'))
    available = models.BooleanField(default=True, verbose_name=gettext_lazy('available'))
    author = models.ForeignKey(User, verbose_name=gettext_lazy('author'), related_name='%(class)s_author',
                               on_delete=models.SET_DEFAULT, default=1, blank=True, editable=False)
    url = models.URLField(null=True)

    @classmethod
    def model_field_exists(cls, field):
        try:
            cls._meta.get_field(field)
            return True
        except models.FieldDoesNotExist:
            return False

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        abstract = True


class Category(BlogModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='category_parent',
                               verbose_name=gettext_lazy('category_parent'), null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('blog:blog_dispatcher', args=[self.url])

    def clean(self):
        smodel.not_self_i_me_parent(self)
        smodel.wrong_hierarchy(self, Category)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        self.url = smodel.compile_url(self)

        super(Category, self).save(self, *args, **kwargs)

    class Meta:
        verbose_name = gettext_lazy('verbose_category_name')
        verbose_name_plural = gettext_lazy('verbose_category_name_plural')


class Post(BlogModel):
    description = models.TextField(verbose_name=gettext_lazy('description'), default='', blank=True)
    short_description = models.TextField(verbose_name=gettext_lazy('short_description'), default='', blank=True)
    image = models.ImageField(upload_to='images/post/', verbose_name=gettext_lazy('post_image'), null=True, blank=True)
    optimized_image = models.ImageField(upload_to='images/post/optimized', verbose_name=gettext_lazy('post_image'),
                                        null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='images/post/thumbnail', verbose_name=gettext_lazy('post_image'),
                                        null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='post_category',
                                 verbose_name=gettext_lazy('category'), null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='post_tags', verbose_name=gettext_lazy('tags'),
                                  null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        self.url = smodel.compile_url(self)
        super(Post, self).save(self, *args, **kwargs)

        # if self.image:
        #     task_img_optimize('images/post/optimized', self.id)
        #     task_create_thumbnail('images/post/thumbnail', self.id)

    def get_breadcrumbs(self):
        return smodel.compile_breadcrumbs(self)

    def get_absolute_url(self):
        return reverse_lazy('blog:blog_dispatcher', args=[self.url])

    class Meta:
        verbose_name = gettext_lazy('verbose_post_name')
        verbose_name_plural = gettext_lazy('verbose_post_name_plural')


register(Category)
register(Post)
