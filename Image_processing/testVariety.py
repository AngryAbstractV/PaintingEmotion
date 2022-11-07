#test cases for harmony feature
# 
import unittest
from variety import calcVariety, calcVariance, get_hist, calcScore, maxVariance
from painting import Painting
import numpy as np

"""
#all test paintings in initial order. this order will change if we change the harmony calculation
#if you run these remove the 'assert greater' statements in test_calc_harmony
testPaintingAddresses = [
    ["ExamplePaintings/fruits.jpg", 0],
    ["ExamplePaintings/mountain.jpg", 0],
    ["ExamplePaintings/test.jpg", 0],
    ["ExamplePaintings/statue.jpg", 0],
    ["ExamplePaintings/versailles.jpg", 0],
    ["ExamplePaintings/monet.jpg", 0],
    ["ExamplePaintings/garden.jpg", 0],
    ["ExamplePaintings/circles.jpg", 0],
    ["ExamplePaintings/olive_trees.jpg", 0],
    ["ExamplePaintings/umbrellas.jpg", 0],
    ["ExamplePaintings/realugly.jpg", 0],
    ["ExamplePaintings/park.png", 0],
    ["ExamplePaintings/bigcolor.jpg", 0],
    ["ExamplePaintings/abstractugly.jpg", 0]
    ]

"""
#3 extreme test paintings. this order shouldn't change
testPaintingAddresses = [
    ["ExamplePaintings/fruits.jpg", 0],
    ["ExamplePaintings/garden.jpg", 0],
    ["ExamplePaintings/abstractugly.jpg", 0]
    ]



class TestVariety(unittest.TestCase):

    def test_get_hist(self):
        return
    
    def test_calc_variance(self):
        return


    def test_max_variance(self):
        return

    def test_calc_score(self):
        return

    def test_calc_variety(self):
        for painting in testPaintingAddresses:
            painting1 = Painting("test", painting[0])
            painting1.preprocessing()
            painting[1] = calcVariety(painting1.getHSVImage())
            self.assertNotEqual(painting[1], 0)
        #self.assertGreater(testPaintingAddresses[0][1], testPaintingAddresses[1][1])
        #self.assertGreater(testPaintingAddresses[1][1], testPaintingAddresses[2][1])
        print(testPaintingAddresses)

if __name__=='__main__':
    unittest.main()