import time

import cv2
import numpy as np

"""
    Gradation is based on change of colors or density throughout an image. The program below
    uses a 3x3 matrix of 1s. It's utilized by scanning the image in a 3x3 small grid and checks
    the pixel change. Scores are tallied up by taking the absolute difference in pixels and adding
    back on top of the final versions of horizontal and vertical scores. 
    It takes a long time to get the scores, need to optimize
    - STILL NOT DONE -
    - Daniel Martinez -
"""


def calc_pixel_change(matrix):
    x, y, z = matrix.shape
    vertical_score = 0
    horizontal_score = 0
    for i in range(x):
        horizontal_score += np.abs(np.diff(matrix[i, i, :], n=x - 1))[0]  # Don't ask me what this does
        vertical_score += np.abs(np.diff(matrix[:, i, i], n=y - 1))[0]  # I will cry if you do
    return vertical_score, horizontal_score


def gradation_score(image, kernel):
    m, n = kernel.shape
    y, x, z = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # the gradient magnitude images are now of the floating point data
    # type, so we need to take care to convert them back a to unsigned
    # 8-bit integer representation so other OpenCV functions can operate
    # on them and visualize them
    gX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    gY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    # compute the gradient magnitude and orientation
    magnitude = np.sqrt((gX ** 2) + (gY ** 2))
    og = cv2.sumElems(magnitude)
    og = og[0]

    while (og >= 100.0):
        og = og % 100


    return 100 - og


def calcGradation(hsvImg):
    print(gradation_score(hsvImg, np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])))


# Set up this way to run just this file and not the main image processing stuff
img = cv2.imread('../ExamplePaintings/gradation.png')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
calcGradation(img)
