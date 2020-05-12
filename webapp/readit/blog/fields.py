from django.db import models


class BlogImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        print('*' * 15)
        print([args, kwargs])
        print('*' * 15)
        super().__init__(*args, **kwargs)
