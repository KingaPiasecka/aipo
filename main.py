import sys

import cv2
#  https://docs.google.com/document/d/1FYA7sAsL-DHlWLmTiyl0b983c0Su3eKj9iDBDHHe-5k/edit?usp=sharing
from segmentationAndScaling import segment
from segmentationAndScaling import scale
from imagePreprocessing import preprocessing
from rotation import rotate, rotate2
from skeletonisation import skeletonize
from characteristic import thirdMethod, fourthMethod
import numpy as np

# wczytanie obrazu
image = cv2.imread('testing4.png')
image2 = image
# Przygotowanie wstepne obrazu
image = preprocessing(image)
image = rotate2(image)
# cv2.imshow('Obraz po obrobce wstepnej', image)

##############################

# Segmentacja obrazu na litery
segmentedImage, characters = segment(image)
cv2.imshow('Obraz po segmentacji', segmentedImage)

skeleton = skeletonize(characters[15])
ready = scale(skeleton, 40)

cv2.imwrite("skel2.png", ready)

# # Rozmiar obrazu po skalowaniu
# dim = 40
# # Rozmiar obszaru dla metody ekstrakcji cech
# rec = 4
#
# fourthMethodOn = True
#
# if fourthMethodOn:
#     rec = 10
#
# samples = np.empty((0, rec*rec), np.float32)
# responses = []
#
#
# for character in characters:
#     cv2.imshow('Litera', character)
#
#     # Skalowanie i szkieletyzacja liter
#     skeleton = skeletonize(character)
#     ready = scale(skeleton, dim)
#
#     cv2.imshow('Ready', ready)
#     key = cv2.waitKey(0)
#     if key == 27:
#         cv2.destroyAllWindows()
#         sys.exit()
#
#     if key == 32:
#         continue
#     else:
#         if fourthMethodOn:
#             vector = fourthMethod(ready)
#         else:
#             vector = thirdMethod(ready, rec)
#         sample = np.float32(vector)
#         sample = sample.reshape((1, rec*rec))
#         samples = np.append(samples, sample, 0)
#         responses.append(key)
#
#     cv2.destroyWindow("Litera")
#     cv2.destroyWindow("Ready")
#
# responses = np.array(responses, np.str)
# responses = responses.reshape((responses.size, 1))
# print "training complete"
#
# samples = np.float32(samples)
# responses = np.float32(responses)
#
# if fourthMethodOn:
#     samplesData = open('samples4.data', 'ab')
#     responsesData = open('responses4.data', 'ab')
# else:
#     samplesData = open('samples3.data', 'ab')
#     responsesData = open('responses3.data', 'ab')
#
# np.savetxt(samplesData, samples)
# np.savetxt(responsesData, responses)
#
# samplesData.close()
# responsesData.close()
#
# cv2.destroyAllWindows()
