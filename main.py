import cv2

from segmentationAndScaling import segment_and_scale
from imagePreprocessing import preprocessing
from rotation import rotate
from skeletonisation import skeletonize
import numpy as np

image = cv2.imread('ocr4.png')
image = preprocessing(image)
image = rotate(image)

#show results
cv2.imshow('rotated', image)


##############################

characters = segment_and_scale(image)
img = characters[0]
cv2.imshow('img', img)
cv2.moveWindow('img', 90, 90)

skel = skeletonize(img)

cv2.imshow('skel', skel)
cv2.moveWindow('skel', 150, 90)
cv2.imwrite("skel.png", skel)


cv2.waitKey()
cv2.destroyAllWindows()