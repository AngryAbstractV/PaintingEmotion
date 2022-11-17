
'''
@author Sinh Mai
@version 0.1
@date 11/16/2022
'''

import numpy as np
import cv2

'''
Algorithm
1. Convert image to GreyScale.
2. For each direction: Vertical, Horizontal (Diagonals optional)
    a. Slice image in half.
    b. Flip one half and subtract it from the other half.
    c. Average the values of the difference matrix.
    c. Subtract the average from 1 .
    
Option 1    
    3. Average the values of the vertical and horizontal symmetries
    4. Output (1 - result of step 3) 
    
Option 2
    3. output the highest average of the two directions

Notes:
1 = perfect symmetry
0 = no symmetry
'''

def bilateralSymmetry(img):
    
    img_hSplit = np.split(img, 2, 0)
    img_vSplit = np.split(img, 2, 1)

    v_difference = abs(img_vSplit[0] - np.fliplr(img_vSplit[1]))
    v_symmetry = np.average(v_difference)

    h_difference = abs(img_hSplit[0] - np.flipud(img_hSplit[1]))
    h_symmetry = np.average(h_difference)
    
    return (v_symmetry, h_symmetry)

def calcBalance(img):
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img/255

    symmetry = bilateralSymmetry(img)

    #max value of either horizontal symmetry vs vertical symmetry

    if (symmetry[0] > symmetry[1]):
        val_min= symmetry[1] 
    else:
        val_min = symmetry[0] 

    #average of both horizontal and vertical symmetry
    val_average = np.average(symmetry)

    return ((1 - val_min), (1- val_average))

if __name__=='__main__':
    
    testImg = "ExamplePaintings/testImg.png"

    img = cv2.imread(testImg)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    val = calcBalance(img)

    print(val)