"""
Date: 03/07/19

Some common arguments for all shapes:
- img, color, thickness, lineType

*) Press 'q' to close the image window
"""
import cv2
import numpy as np


def draw_line(img=None):
    img = get_image(img)
    img = cv2.line(img, (0, 0), (512, 512), (255, 0, 140), 2)
    display_image(img)


def get_image(img):
    if img is None:
        img = np.zeros((512, 512, 3), np.uint8)
    return img


def draw_rect(img=None):
    img = get_image(img)
    img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    display_image(img)


def display_image(img):
    if img is None:
        print("Image does not exist")
        return
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# draw_line()
draw_rect()
