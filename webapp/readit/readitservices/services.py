from django.conf import settings
from PIL import Image
from django.core.files.storage import default_storage as storage
import os


def create_thumbnail(image_path, destination_path, area=(30, 30, 110, 110)):
    """Wrapper on Pillow.Image.crop"""
    with Image.open(image_path) as image:
        file_name = os.path.basename(image_path).split('.')[0]

        width, height = image.size

        image.thumbnail((width / 4, height / 4))
        i_crop = image.crop(area)
        i_width, i_height = i_crop.size
        i_crop.n_file_name = f"{file_name}_{i_width}x{i_height}.{image.format}"
        i_crop.destination_path = os.path.join(destination_path, i_crop.n_file_name)
        i_crop.save(i_crop.destination_path)

    return i_crop.destination_path


def img_optimize(upload_to=None, image_path=None, quality=70):
    """Wrapper on  Pillow.Image.save"""

    upload_to_ = os.path.realpath(os.path.join(settings.MEDIA_ROOT, upload_to))
    image_path = storage.open(image_path.name, 'r')

    with Image.open(image_path) as image:
        file_name = image_path.split('/')[-1]
        image.n_file_name = file_name.lower()
        image.destination_path = image_path_
        image.save(image_path_, image.format, optimize=True, quality=quality)

    return os.path.realpath(os.path.join(upload_to, image_path))


def resize(image_path, destination_path, ratio: float):
    """Wrapper on  Pillow.Image.resize"""
    with Image.open(image_path) as image:
        file_name = os.path.basename(image_path).split('.')[0]

        width, height = int(image.width * ratio), int(image.size[1] * ratio)

        image.n_file_name = f"{file_name}_{width}x{height}.{image.format.lower()}"
        image.destination_path = os.path.join(destination_path, image.n_file_name)
        r_img = image.resize((width, height), Image.ANTIALIAS)
        r_img.save(image.destination_path, image.format)

    return r_img.destination_path


def create_thumbnail(upload_to=None, image_path=None, size=[80, 80]):
    """Wrapper on Pillow.Image.thumbnail"""

    upload_to_ = os.path.realpath(os.path.join(settings.MEDIA_ROOT, upload_to))
    image_path = storage.open(image_path.name, 'r')

    with Image.open(image_path) as image:
        height = size[1] if size[1] else image.height
        width = size[0] if size[0] else image.width

        image.thumbnail((width, height))
        file_name = image_path.split('/')[-1]
        image.n_file_name = file_name.lower()
        image.destination_path = image_path_
        image.save(image_path_, image.format)

    return os.path.realpath(os.path.join(upload_to, image_path))
