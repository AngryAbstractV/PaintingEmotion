#test cases for harmony feature
# 
import unittest
from harmony import calcHarmony, calcModeHarmony, calcPixelHarmony, genNeighborhoodHistogram
from painting import Painting
import numpy as np


#all test paintings in initial order. this order will change if we change the harmony calculation
#if you run these remove the 'assert greater' statements in test_calc_harmony
testPaintingAddresses = [
    ["../ExamplePaintings/fruits.jpg", 0],
    ["../ExamplePaintings/mountain.jpg", 0],
    ["../ExamplePaintings/test.jpg", 0],
    ["../ExamplePaintings/statue.jpg", 0],
    ["../ExamplePaintings/versailles.jpg", 0],
    ["../ExamplePaintings/monet.jpg", 0],
    ["../ExamplePaintings/garden.jpg", 0],
    ["../ExamplePaintings/circles.jpg", 0],
    ["../ExamplePaintings/olive_trees.jpg", 0],
    ["../ExamplePaintings/umbrellas.jpg", 0],
    ["../ExamplePaintings/realugly.jpg", 0],
    ["../ExamplePaintings/park.png", 0],
    ["../ExamplePaintings/bigcolor.jpg", 0],
    ["../ExamplePaintings/abstractugly.jpg", 0]
    ]

"""
#3 extreme test paintings. this order shouldn't change
testPaintingAddresses = [
    ["ExamplePaintings/fruits.jpg", 0],
    ["ExamplePaintings/garden.jpg", 0],
    ["ExamplePaintings/abstractugly.jpg", 0]
    ]
"""



class TestHarmony(unittest.TestCase):

    def test_gen_neighborhood_histogram(self):
        array1 = np.arange(75).reshape(5,5,3)
        self.assertEqual(genNeighborhoodHistogram(array1),[8,7,8,2,0,0,0,0])
    
    def test_calc_mode_harmony(self):
        modes1 = [[1, 81],[0,0]]
        self.assertEqual(calcModeHarmony(modes1), 4.0)
        modes1 = [[6,81],[0,0]]
        self.assertEqual(calcModeHarmony(modes1), 4.0)
        modes1 = [[3,20],[6,20]]
        self.assertEqual(calcModeHarmony(modes1), 3.0)
        modes1 = [[3,20],[6,15]]
        self.assertEqual(round(calcModeHarmony(modes1), 4), 0.0202)


    def test_calc_pixel_harmony(self):
        histogram1 = [0,0,0,10,0,0,0,0]
        self.assertEqual(calcPixelHarmony(histogram1), 4.0)
        histogram1 = [0,20,0,20,0,0,0,0]
        self.assertEqual(calcPixelHarmony(histogram1), 2.0)
        histogram1 = [20,0,0,0,0,0,20,0]
        self.assertEqual(calcPixelHarmony(histogram1), 2.0)
        histogram1 = [5,6,8,4,3,6,10,6]
        self.assertEqual(round(calcPixelHarmony(histogram1),4), 0.5413)

    def test_calc_harmony(self):
        for painting in testPaintingAddresses:
            painting1 = Painting("test", painting[0])
            painting1.preprocessing()
            painting[1] = calcHarmony(painting1.getHSVImage())
            self.assertNotEqual(painting[1], 0)
        self.assertGreater(testPaintingAddresses[0][1], testPaintingAddresses[1][1])
        self.assertGreater(testPaintingAddresses[1][1], testPaintingAddresses[2][1])
        print(testPaintingAddresses)

if __name__=='__main__':
    unittest.main()