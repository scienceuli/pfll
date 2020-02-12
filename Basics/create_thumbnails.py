# create_thumbnails.py

import os
import glob
import fnmatch
import pathlib

from PIL import Image


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


path = "/Users/scienceuli/Projekte/DBBay/Bayern8/Verlag_an"
target = "./thumbnails"

thumb_width = 100


for file in pathlib.Path(path).rglob('*.eps'):
    im = Image.open(file)
    im_thumb = crop_max_square(im).resize(
        (thumb_width, thumb_width), Image.LANCZOS)

    im_thumb.save(os.path.join(target, file.stem +
                               '_thumbnail' + ".eps"), quality=95)
