from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy


class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse_lazy("tag:tag_posts", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
