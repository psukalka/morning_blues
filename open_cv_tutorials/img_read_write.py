"""
Reading and writing an image with Open CV.
Numpy is an important library for most opencv operations. Deep understanding of it will be helpful.

*) Even if the image path is wrong, it won’t throw any error, but print img will give you None
*) Color image loaded by OpenCV is in BGR mode while by matplotlib is in RGB mode.
"""
import cv2
import os

'''
cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
'''


def display_image(img):
    img_resize = cv2.resize(img, (1600, 900))
    cv2.imshow('image', img_resize)
    print("Press ESC key to kill the window")
    k = cv2.waitKey(0)  # Waits indefinitely
    if k == 27:
        cv2.destroyAllWindows()


def convert_to_png(img, name="candid.png"):
    # Size of original image was 3.7M and that of PNG was 17M
    ext = os.path.splitext(name)[1]
    if ext != ".png":
        print("Image extension {} is not correct. Only png extension is allowed. Exiting...".format(ext))
        exit(1)
    cv2.imwrite(name, img)


cv2.namedWindow("image", cv2.WINDOW_NORMAL)
img_dir = "/Users/pavansukalkar/Desktop/2018/"
img_name = "candid.jpg"
image = cv2.imread('{}{}'.format(img_dir, img_name), -1)
display_image(image)
# convert_to_png(image, name=img_dir + "candid.png")
