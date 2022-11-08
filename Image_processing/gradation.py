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
    horizontal_score = 0
    vertical_score = 0
    # Iteration of all pixels in the image
    # Loops are in range to not fall out of bounds
    optimized = time.time()
    for i in range(y - n + 1):
        for j in range(x - n + 1):
            if j % 3 == 0 and i % 3 == 0:
                current_matrix = kernel * (image[i:i + m, j:j + n])  # Copy current pixels onto 3x3 matrix
                horizontal_score += np.abs(np.diff(current_matrix[0, 0, :], n=2))[0]
                vertical_score += np.abs(np.diff(current_matrix[:, 0, 0], n=2))[0]
                horizontal_score += np.abs(np.diff(current_matrix[1, 1, :], n=2))[0]
                vertical_score += np.abs(np.diff(current_matrix[:, 1, 1], n=2))[0]
                horizontal_score += np.abs(np.diff(current_matrix[2, 2, :], n=2))[0]
                vertical_score += np.abs(np.diff(current_matrix[:, 2, 2], n=2))[0]
    print(time.time() - optimized)
    print(vertical_score)
    print(horizontal_score)
    # newTotal = vertical_score + horizontal_score
    # vertical_score = 0
    # horizontal_score = 0

    # old = time.time()
    # for i in range(y - n + 1):
    #    for j in range(x - n + 1):
    #        current_matrix = kernel * (image[i:i + m, j:j + n])  # Copy current pixels onto 3x3 matrix
    #        horizontal_score += np.abs(np.diff(current_matrix[0, 0, :], n=2))[0]
    #        vertical_score += np.abs(np.diff(current_matrix[:, 0, 0], n=2))[0]
    #        horizontal_score += np.abs(np.diff(current_matrix[1, 1, :], n=2))[0]
    #        vertical_score += np.abs(np.diff(current_matrix[:, 1, 1], n=2))[0]
    #        horizontal_score += np.abs(np.diff(current_matrix[2, 2, :], n=2))[0]
    #        vertical_score += np.abs(np.diff(current_matrix[:, 2, 2], n=2))[0]

    # print(time.time() - old)
    # print(vertical_score)
    # print(horizontal_score)
    # oldTotal = vertical_score + horizontal_score
    # print(np.diff([newTotal, oldTotal]))

    return (vertical_score // (x * y)) + (horizontal_score // (x * y))  # Dividing by size to make it a smaller score


def calcGradation(hsvImg):
    print(gradation_score(hsvImg, np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])))


# Set up this way to run just this file and not the main image processing stuff
img = cv2.imread('../ExamplePaintings/statue.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
calcGradation(hsv_img)
