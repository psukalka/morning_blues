"""
Date: 05/07/19

Understanding basic image operations in OpenCV
Since these are mostly numeric, having good knowledge of numpy is recommended

*) Numpy is an optimized library for fast array calculations, so simply accessing each and every pixel value will be slow
    and is discouraged.
*) dtype is a very important property while debugging as most of errors in opencv are due to invalid datatype.
*) cv2.split() is a costly operation(in terms of time) and should be used only if necessary.
    Numpy indexing is much more efficient and should be used instead if possible.

"""

import cv2
from utils.img_utils import display_image


def get_image_shape(image=None):
    image = get_image(image)
    print("shape: {}".format(image.shape))
    print("size: {}".format(image.size))
    print("data type: {}".format(image.dtype))


# Region of interest
def select_roi(image=None):
    image = get_image(image)
    roi = image[2200:2500, 1500:1700]
    print(roi)
    # Cropped and pasted a region in another part of image
    image[100:400, 100:300] = roi
    display_image(image)


def splitting_channels(image=None):
    image = get_image(image)
    b, g, r = cv2.split(image)
    print(b.shape)
    # Displaying only a channel will display a grey image
    display_image(b)


def display_channel(image=None, channel=0):
    image = get_image(image)
    img_copy = image.copy()
    for i in range(0, 3):
        if i == channel:
            continue
        img_copy[:,:,i] = 0
    display_image(img_copy)


def get_image(image):
    if image is None:
        img_dir = "/Users/pavansukalkar/Desktop/2018/"
        img_name = "candid.jpg"
        image = cv2.imread('{}{}'.format(img_dir, img_name), 1)
    return image


# get_image_shape()
# select_roi()
# splitting_channels()
display_channel(channel=1)