import cv2

from segmentationAndScaling import segment_and_scale
from imagePreprocessing import preprocessing
from rotation import rotate, rotate2
from skeletonisation import skeletonize
from secondMethod import secondMethod, thirdMethod
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

skel = skeletonize(img)
m2 = thirdMethod(skel,9)
print(m2)
cv2.imshow('skel', skel)
cv2.moveWindow('skel', 150, 90)
cv2.imwrite("skel.png", skel)


cv2.waitKey()
cv2.destroyAllWindows()

##############################

#Ekstrakcja wektorow cech z liter
#Porownanie wektorow cech liter z wektorami cech probek treningowych