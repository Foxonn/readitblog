from PIL import Image
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


def optimize(image_path, destination_path, quality_=85):
    """Wrapper on  Pillow.Image.save"""
    with Image.open(image_path) as image:
        file_name = os.path.basename(image_path).split('.')[0]
        image.n_file_name = f"{file_name}_opt.{image.format.lower()}"
        image.destination_path = os.path.join(destination_path, image.n_file_name)
        image.save(image.destination_path, image.format, optimize=True, quality=quality_)

    return image.destination_path


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


def thumbnail(image_path, destination_path, size):
    """Wrapper on Pillow.Image.thumbnail"""
    with Image.open(image_path) as image:
        file_name = os.path.basename(image_path).split('.')[0]

        height = size[1] if size[1] else image.height
        width = size[0] if size[0] else image.width

        image.thumbnail((width, height))
        image.n_file_name = f"{file_name}_{image.height}x{image.width}.{image.format.lower()}"
        image.destination_path = os.path.join(destination_path, image.n_file_name)
        image.save(image.destination_path, image.format)

    return image.destination_path
