"""
Date: 07/07/19

Create a slideshow of images in a folder
"""
import cv2
import os
from utils.img_utils import display_image


def slideshow(dir_path):
    files = get_files_in_folder(dir_path)
    prev_img = None
    for file_ in files:
        # Display only jpg files
        if file_.endswith(".jpg"):
            img = cv2.imread(os.path.join(dir_path, file_))
            if prev_img is not None:
                print("transitioning image: {}".format(file_))
                image_transition(img, prev_img)
            else:
                print("displaying image: {}".format(file_))
                display_image(img, wait_key=2000, destroy_windows=False)
            prev_img = img
        else:
            print("File: {} will not be displayed".format(file_))


def image_transition(img, prev_img):
    display_image(prev_img, wait_key=3000, destroy_windows=False)
    img = cv2.resize(img, (1600, 900))
    prev_img = cv2.resize(prev_img, (1600, 900))
    print("resized images")
    for alpha in range(0, 6):
        mix = cv2.addWeighted(prev_img, (5 - alpha) / 5.0, img, alpha / 5.0, 0)
        display_image(mix, wait_key=50, destroy_windows=False)


def get_files_in_folder(dir_path):
    print("getting files in : {}".format(dir_path))
    return os.listdir(dir_path)


folder_path = "/Users/pavansukalkar/Desktop/2018"
slideshow(folder_path)
