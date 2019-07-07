"""
Date: 06/07/19

*) Opencv addition is a saturated operation while numpy addition is a modulo operation.
*) TypeError: Expected cv::UMat for argument 'src2' --> Type of two arguments are different.
"""
import numpy as np
import cv2

from utils.img_utils import display_image


def add_images(x=[], y=[]):
    x = np.uint8([250])
    y = np.uint8([10])

    z = cv2.add(x, y)
    z2 = x + y

    print("Open CV way: {}, shape: {}".format(z, z.shape))
    print("Numpy Way: {}, shape: {}".format(z2, z2.shape))

    # Similarly weight addition can give a cool transition effect.


def paste_logo_over_image(img1, img2):
    # Creating region of interest
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]

    # Create mask of logos and its inverse mask.
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255,
                              cv2.THRESH_BINARY)  # This will enhance contrast thus showcasing logo in white
    inv_mask = cv2.bitwise_not(mask)

    # Blackout area of logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=inv_mask)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # Put log in image
    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst

    display_image(img1)

img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv_logo.png')
add_images(img1, img2)
