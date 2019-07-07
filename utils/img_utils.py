"""
Image related utilities
"""
import cv2
import numpy as np


def display_image(img, wait_key=0, destroy_windows=True):
    if img is None:
        print("Image does not exist")
        return
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(wait_key)
    if destroy_windows:
        cv2.destroyAllWindows()


def get_image(img):
    if img is None:
        img = np.zeros((512, 512, 3), np.uint8)
    return img
