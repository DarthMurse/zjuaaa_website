import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

thumbnail_maxWidth = 1280
thumbnial_maxHeight = 1280

origin_path = "../origin1/"
file_name = "xyjj1.jpg"

file_name_save_head = "xyjj1"

file_name_head, file_extension = os.path.splitext(file_name)

src = cv2.imread(origin_path + file_name)


def process_full(src, dst, file_name_head):
    cv2.imwrite(dst + file_name_head + ".png", src)


def draw_histogram(src, dst, file_name_head):

    hist_b = cv2.calcHist([src], [0], None, [256], [0, 256]).reshape(-1)
    hist_g = cv2.calcHist([src], [1], None, [256], [0, 256]).reshape(-1)
    hist_r = cv2.calcHist([src], [2], None, [256], [0, 256]).reshape(-1)

    max_h = np.max([hist_b, hist_g, hist_r])

    hist_b /= max_h
    hist_g /= max_h
    hist_r /= max_h

    array_img = np.zeros([128, 257, 4], dtype=np.uint8)

    for i in range(256):
        for j in range(128):
            if (j / 128 < hist_b[i]):
                array_img[127 - j, i][0] = 255
                array_img[127 - j, i][3] = 255
            else:
                array_img[127 - j, i][0] = 0
            if (j / 128 < hist_g[i]):
                array_img[127 - j, i][1] = 255
                array_img[127 - j, i][3] = 255
            else:
                array_img[127 - j, i][1] = 0
            if (j / 128 < hist_r[i]):
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

    array_img = cv2.addWeighted(array_img, 1, grid_img, 0.5, 0)
    # cv2.imshow("histogram", array_img)
    cv2.imwrite(dst + "histogram_" + file_name_head + ".png", array_img)

    # plt.figure("histogram")

    # plt.plot(hist_b, color='b')
    # plt.plot(hist_g, color='g')
    # plt.plot(hist_r, color='r')

    # plt.xlim([0, 255])
    # plt.show()


def draw_thumbnail(src, dst, file_name_head):
    height, width = src.shape[:2]
    w_ratio = width / thumbnail_maxWidth
    h_ratio = height / thumbnial_maxHeight
    if (w_ratio > 1 and h_ratio > 1):
        if (w_ratio > h_ratio):
            dim = (thumbnail_maxWidth, int(height / w_ratio))
        else:
            dim = (int(width / h_ratio), thumbnial_maxHeight)
    else:
        dim = (width, height)
    resized = cv2.resize(src, dim, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(dst + "thumbnail_" + file_name_head + ".png", resized)


dst_full = "masterpiece/full/"
dst_hist = "masterpiece/histogram/"
dst_thumbnail = "masterpiece/thumbnail/"

process_full(src, dst_full, file_name_save_head)
draw_histogram(src, dst_hist, file_name_save_head)
draw_thumbnail(src, dst_thumbnail, file_name_save_head)
print("Done!")