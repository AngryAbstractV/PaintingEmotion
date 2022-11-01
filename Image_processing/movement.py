#movement calculation: written initially by Nicole and Lettie
import math
import numpy as np

#HUE = 0 - 180 (179?)
#SATURATION = 0 - 255
#VALUE = 0 - 255


def genSaliencyMap(img):
    #generate saliency map
    return saliencyMap


def genAvgSacadeLength(saliencyMap, mapLength):
    #create list (of length maplength) of most salient points salientList
    #of form [[x,y], [x,y], [x,y], ...]

    sacades = 0
    #for x in range(mapLength-1):
    # √[(x₂ - x₁)² + (y₂ - y₁)²] 
    #distance = sqrt(( salientList[x][0]- salientList[x+1][0])² + (salientList[x][1]- salientList[x+1][1])²)
    #sacades += distance

    return (sacades / (mapLength-1))


def calcMovement(img):
    salienceMap = genSalinecyMap(img)

    standardDev = 0 # get s.d. of saliency values (in the map)
    maplength = 0 # (s.d * (height*width of saliency map))

    avgSacadeLength = genAvgSacadeLength(salienceMap, maplength)

    saliency = standardDev * avgSacadeLength #some normalized value combinding these
    return saliency


