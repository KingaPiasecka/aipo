import cv2
import numpy as np
from rotation import rotate
from segmentationAndScaling import segment_and_scale

#Read image
img = cv2.imread('ocr4.png')

#Convert to gray
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Histogram equalization - psuje..
#img = cv2.equalizeHist(img)

#create a CLAHE object - Normalizacja histogramu CLAHE, praktycznie nic nie zmienia
clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(1,1))
img = clahe.apply(img)

#Apply threshold to get image with only black and white - binarization
#blur = cv2.GaussianBlur(img,(5,5),0) #Gaussian Filtering
#ret3,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

th, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#Apply dilatation and erosion to remove some noise
kernel = np.ones((1,1), np.uint8)
img = cv2.erode(img, kernel, iterations=1)
#img = cv2.dilate(img, kernel, iterations=2)

#ewentualna dodatkowa filtracja
img = cv2.GaussianBlur(img,(1,1),0)

rotated = rotate(img)
#show results
cv2.imshow('rotated',rotated)
cv2.waitKey()
