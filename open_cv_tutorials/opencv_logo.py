"""
Date: 04/07/19

Draw open cv logo
"""
from utils.img_utils import display_image, get_image
import cv2


def open_cv_logo(img=None):
    img = get_image(img)
    img = cv2.ellipse(img, (200, 100), (50, 50), 145, 250, 0, (0, 0, 255), 50)  # Red
    img = cv2.ellipse(img, (120, 220), (50, 50), 0, 250, 0, (0, 255, 0), 50)   # Green
    img = cv2.ellipse(img, (280, 220), (50, 50), 320, 250, 0, (255, 0, 0), 50)  # Blue
    display_image(img)


open_cv_logo()
