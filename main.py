import cv2
#  https://docs.google.com/document/d/1FYA7sAsL-DHlWLmTiyl0b983c0Su3eKj9iDBDHHe-5k/edit?usp=sharing
from segmentationAndScaling import segment_and_scale
from imagePreprocessing import preprocessing
from rotation import rotate, rotate2
from skeletonisation import skeletonize
from characteristic import secondMethod, thirdMethod
import numpy as np

# wczytanie obrazu
image = cv2.imread('test2.bmp')
# Przygotowanie wstepne obrazu
image = preprocessing(image)
image = rotate2(image)
cv2.imshow('Obraz po obrobce wstepnej', image)

##############################

# Segmentacja obrazu na litery
# Skalowanie i szkieletyzacja liter

characters = segment_and_scale(image)
img = characters[0]
cv2.imshow('img', img)
cv2.moveWindow('img', 90, 90)
#
# skel = skeletonize(img)
# #m2 = secondMethod(skel) # to cos srednio dziala
# m2 = thirdMethod(skel,3)
# print(m2)
# cv2.imshow('skel', skel)
# cv2.moveWindow('skel', 150, 90)
# cv2.imwrite("skel.png", skel)


cv2.waitKey()
cv2.destroyAllWindows()
