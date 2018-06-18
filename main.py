import cv2

from segmentationAndScaling import segment_and_scale

characters = segment_and_scale('training_image.png')

img = characters[0]
print len(characters)
cv2.imshow('dst', img)
cv2.moveWindow('dst', 40,30)
cv2.waitKey()