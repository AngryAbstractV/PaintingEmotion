#movement calculation: written initially by Nicole and Lettie
import math
import numpy as np
import cv2

#HUE = 0 - 180 (179?)
#SATURATION = 0 - 255
#VALUE = 0 - 255

def resize(img):
    pix_threshold = 500
    img_wid = img.shape[1]
    img_len = img.shape[0]

    new_wid = 0
    new_len = 0

    if img_wid > pix_threshold or img_len > pix_threshold:
        # find out which is bigger
        if img_wid > img_len:
            new_wid = pix_threshold
            scale = (new_wid * 100) // img_wid
            new_len = (img_len * scale) // 100
        elif img_len > img_wid:
            new_len = pix_threshold
            scale = (new_len * 100) // img_len
            new_wid = (img_wid * scale) // 100
        else:
            # wid and len are equal
            new_wid = pix_threshold
            new_len = pix_threshold
    else:
        return img

    dim = (new_wid, new_len)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized


def displayPath(img, salientList, mapLength):
    for x in range(mapLength - 1):
        # draw a line starting at [x] and ending at [x+1]
        # if x % 9 == 0:
        #     img = cv2.line(img, salientList[x], salientList[x+1], (0, 255, 0), 1)
        img = cv2.line(img, salientList[x], salientList[x+1], (0, 255, 0), 1)
    return img

def genSaliencyMap(image):
    # returns an image that is the saliency map
    # https://pyimagesearch.com/2018/07/16/opencv-saliency-detection/

    saliency = cv2.saliency.StaticSaliencyFineGrained_create()
    (success, saliencyMap) = saliency.computeSaliency(image)
    return saliencyMap


def genAvgSacadeLength(saliencyMap, mapLength):
    #create list (of length maplength) of most salient points salientList
    #of form [[x,y], [x,y], [x,y], ...]

    salientList = np.argpartition(saliencyMap, saliencyMap.size - mapLength, axis=None)[-mapLength:]
    salientList = np.column_stack(np.unravel_index(salientList, saliencyMap.shape))

    sacades = 0
    #for x in range(mapLength-1):
    # √[(x₂ - x₁)² + (y₂ - y₁)²] 
    #distance = sqrt(( salientList[x][0]- salientList[x+1][0])² + (salientList[x][1]- salientList[x+1][1])²)
    #sacades += distance

    for x in range(mapLength - 1):
        # √[(x₂ - x₁)² + (y₂ - y₁)²] 
        distance = math.sqrt(abs((salientList[x][0] - salientList[x+1][0]) ** 2 + (salientList[x][1] - salientList[x+1][1] ** 2)))
        sacades += distance

    return ((sacades / (mapLength - 1)), salientList)


def calcMovement(img):
    salienceMap = genSaliencyMap(img)

    cv2.imshow("Image", salienceMap)
    cv2.imshow("Image2", img)
    cv2.waitKey(0)

    standardDev = np.std(salienceMap)
    maplength = int(standardDev * salienceMap.shape[0] * salienceMap.shape[1])

    print("map length: " + str(maplength))
    print("std: " + str(standardDev))

    (avgSacadeLength, salientList) = genAvgSacadeLength(salienceMap, maplength)

    saliency = standardDev * avgSacadeLength #some normalized value combining these



    img = displayPath(img, salientList, maplength)
    cv2.imshow("Image3", img)
    cv2.waitKey(0)

    return saliency



# -------------------------------

filename = 'images/umbrellas.jpg'
img = cv2.imread(filename, 1)
img = resize(img)

print(filename)
print("movement: " + str(calcMovement(img)))

