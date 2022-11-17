
'''
@author Sinh Mai
@version 0.1
@date 11/16/2022
'''

import numpy as np
import cv2 as cv

'''
Steps
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

def basicSymmetry(img):
    
    
    
    return 1