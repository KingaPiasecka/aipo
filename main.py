import cv2

from segmentationAndScaling import segment_and_scale
from imagePreprocessing import preprocessing
from rotation import rotate

image = cv2.imread('ocr4.png')
image = preprocessing(image)
image = rotate(image)

#show results
cv2.imshow('rotated',image)
cv2.waitKey()

characters = segment_and_scale('training_image.png')
img = characters[0]
print len(characters)
cv2.imshow('dst', img)
cv2.moveWindow('dst', 40,30)
cv2.waitKey()


