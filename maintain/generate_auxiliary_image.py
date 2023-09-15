import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image, ImageCms
import io

thumbnail_maxWidth = 360
thumbnial_maxHeight = 360

small_maxWidth = 1280
small_maxHeight = 1280

origin_path = "../origin1/"
file_name = "xyjj1.png"

file_name_save_head = "xyjj1"

file_name_head, file_extension = os.path.splitext(file_name)

src = Image.open(origin_path + file_name)

srgb_icc = ImageCms.createProfile("sRGB")
srgb_icc_bytes = ImageCms.ImageCmsProfile(srgb_icc).tobytes()

print(src.mode)
if (src.mode == "RGB" or src.mode == "RGBA"):
    src_array = np.asarray(src)
    if ((src_array[:, :, 0] == src_array[:, :, 1]).all()
            and (src_array[:, :, 1] == src_array[:, :, 2]).all()):
        if (src.mode == "RGBA"):
            src = Image.merge("LA", [src.getchannel("R"), src.getchannel("A")])
        else:
            src = src.getchannel("R")
        img_icc = None
    else:
        icc_data = src.info.get('icc_profile', None)
        if icc_data is not None:
            icc = ImageCms.ImageCmsProfile(io.BytesIO(icc_data))
            icc_name = ImageCms.getProfileName(icc)
            if "srgb" in icc_name.lower():
                img_icc = icc_data
            else:
                src = ImageCms.profileToProfile(src, icc, srgb_icc)
                img_icc = srgb_icc_bytes
        else:
            img_icc = srgb_icc_bytes
elif (src.mode == "L" or src.mode == "LA"):
    img_icc = None
elif ("I" in src.mode):
    src.convert("L")
    img_icc = None
else:
    print("Error: Unknown mode: " + src.mode)
    exit(1)


def process_full(src, dst, file_name_head):
    src.save(dst + "full_" + file_name_head + ".png", icc_profile=img_icc)


def draw_small(src, dst, file_name_head):
    small_image = src.copy()
    small_image.thumbnail((small_maxWidth, small_maxHeight),
                          resample=Image.Resampling.LANCZOS)
    small_image.save(dst + "small_" + file_name_head + ".png",
                     icc_profile=img_icc)


def draw_thumbnail(src, dst, file_name_head):
    thumbnail_image = src.copy()
    thumbnail_image.thumbnail((thumbnail_maxWidth, thumbnial_maxHeight),
                              resample=Image.Resampling.LANCZOS)
    thumbnail_image.save(dst + "thumbnail_" + file_name_head + ".png",
                         icc_profile=img_icc)


def draw_histogram(src, dst, file_name_head):
    hist_array = src.histogram()

    if (src.mode == "RGB" or src.mode == "RGBA"):
        hist_r = hist_array[0:256]
        hist_g = hist_array[256:512]
        hist_b = hist_array[512:768]

        max_h = np.max([hist_r, hist_g, hist_b])

        hist_r /= max_h
        hist_g /= max_h
        hist_b /= max_h

        array_img = np.zeros([128, 257, 4], dtype=np.uint8)

        for i in range(256):
            for j in range(128):
                if (j / 128 < hist_r[i]):
                    array_img[127 - j, i][0] = 255
                    array_img[127 - j, i][3] = 255
                else:
                    array_img[127 - j, i][0] = 0
                if (j / 128 < hist_g[i]):
                    array_img[127 - j, i][1] = 255
                    array_img[127 - j, i][3] = 255
                else:
                    array_img[127 - j, i][1] = 0
                if (j / 128 < hist_b[i]):
                    array_img[127 - j, i][2] = 255
                    array_img[127 - j, i][3] = 255
                else:
                    array_img[127 - j, i][2] = 0

        grid_img = np.zeros([128, 257, 4], dtype=np.uint8)

        for i in [0, 64, 128, 192, 256]:
            for j in range(128):
                grid_img[127 - j, i][0] = 255
                grid_img[127 - j, i][1] = 255
                grid_img[127 - j, i][2] = 255
                grid_img[127 - j, i][3] = 255

    else:
        hist_L = hist_array[0:256]
        max_h = np.max([hist_L])
        hist_L /= max_h
        array_img = np.zeros([128, 257, 2], dtype=np.uint8)

        for i in range(256):
            for j in range(128):
                if (j / 128 < hist_L[i]):
                    array_img[127 - j, i][0] = 220
                    array_img[127 - j, i][1] = 255

        grid_img = np.zeros([128, 257, 2], dtype=np.uint8)

        for i in [0, 64, 128, 192, 256]:
            for j in range(128):
                grid_img[127 - j, i][0] = 255
                grid_img[127 - j, i][1] = 255

    array_img = np.min(
        [(grid_img * 0.5).astype(np.uint16) + array_img.astype(np.uint16),
         np.ones(array_img.shape, dtype=np.uint16) * 255],
        axis=0).astype(np.uint8)

    hist_img = Image.fromarray(array_img)
    hist_img.save(dst + "histogram_" + file_name_head + ".png",
                  icc_profile=img_icc)


dst_full = "masterpiece/full/"
dst_small = "masterpiece/small/"
dst_thumbnail = "masterpiece/thumbnail/"
dst_hist = "masterpiece/histogram/"

draw_thumbnail(src, dst_thumbnail, file_name_save_head)
draw_small(src, dst_small, file_name_save_head)
draw_histogram(src, dst_hist, file_name_save_head)
process_full(src, dst_full, file_name_save_head)

print("Done!")
