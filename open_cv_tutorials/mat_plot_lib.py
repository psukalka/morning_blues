"""
Date: 01/07/19
Understanding matplotlib library. Using it to display an image.

*) Image displayed with CV2 was not closing, it's easier with matplotlib
*) OpenCV follows BGR order while matplotlib follows RGB order. Hence, there will be color difference if an image read
opencv is displayed using matplotlib. So, convert from BGR2RGB first.
"""

import cv2
from matplotlib import pyplot as plt


def read_image(path="candid.png"):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img = img[:, :, ::-1]   # Numpy convention of flipping color planes
    return img


def display_image_with_mpl(img):
    plt.imshow(img, cmap="gray", interpolation="bicubic")
    plt.xticks([])  # To hide tick values on X axis
    plt.yticks([])  # To hide tick values on Y axis
    plt.show()


image = read_image()
display_image_with_mpl(image)
