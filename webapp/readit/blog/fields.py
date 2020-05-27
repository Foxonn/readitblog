from django.conf import settings
from django.db.models import ImageField
from PIL import Image
import os
import json


class ImagesField(ImageField):

    def __init__(self, verbose_name=None, name=None, width_field=None, height_field=None, **kwargs):
        self.width_field, self.height_field = width_field, height_field
        self.upload_to = kwargs.get('upload_to', None)
        super().__init__(verbose_name, name, **kwargs)

    def from_db_value(self, value, expression, connection):
        return value

    def get_prep_value(self, value):
        value = super(ImageField, self).get_prep_value(value)

        if value:
            optimized = self._optimize(self.upload_to, value)
            thumbnail = self._thumbnail(self.upload_to, value)

            return json.dumps({'original': value, 'optimized': optimized, 'thumbnail': thumbnail})

        return value

    def _thumbnail(self, upload_to=None, image_path=None, destination_dir='thumbnail', size=[80, 80]):
        """Wrapper on Pillow.Image.thumbnail"""

        upload_to_ = os.path.realpath(os.path.join(settings.MEDIA_ROOT, upload_to))
        image_path_ = os.path.realpath(os.path.join(settings.MEDIA_ROOT, image_path))

        with Image.open(image_path_) as image:
            height = size[1] if size[1] else image.height
            width = size[0] if size[0] else image.width

            image.thumbnail((width, height))
            file_name = image_path.split('/')[-1]
            image.n_file_name = file_name.lower()
            image.destination_path = os.path.join(upload_to_, destination_dir, image.n_file_name)
            image.save(image.destination_path, image.format)

        return os.path.join(upload_to, destination_dir, image.n_file_name)

    def _optimize(self, upload_to=None, image_path=None, destination_dir='optimize', quality=70):
        """Wrapper on  Pillow.Image.save"""

        upload_to_ = os.path.realpath(os.path.join(settings.MEDIA_ROOT, upload_to))
        image_path_ = os.path.realpath(os.path.join(settings.MEDIA_ROOT, image_path))

        with Image.open(image_path_) as image:
            file_name = image_path.split('/')[-1]
            image.n_file_name = file_name.lower()
            image.destination_path = os.path.join(upload_to_, destination_dir, image.n_file_name)
            image.save(image.destination_path, image.format, optimize=True, quality=quality)

        return os.path.join(upload_to, destination_dir, image.n_file_name)
