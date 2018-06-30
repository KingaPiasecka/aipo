import numpy as np
import cv2
from imagePreprocessing import preprocessing
from skeletonisation import skeletonize
from characteristic import thirdMethod, fourthMethod
from segmentationAndScaling import scale, segment


image = cv2.imread('test3.bmp')
image = preprocessing(image)

# Rozmiar obrazu po skalowaniu
dim = 40
# Rozmiar obszaru dla metody ekstrakcji cech
rec = 4
fourthMethodOn = True
if fourthMethodOn:
    rec = 10
    samples = np.loadtxt('samples4.data', np.float32)
    responses = np.loadtxt('responses4.data', np.float32)
else:
    samples = np.loadtxt('samples3.data', np.float32)
    responses = np.loadtxt('responses3.data', np.float32)

responses = responses.reshape((responses.size, 1))

knn = cv2.ml.KNearest_create()
knn.train(samples, cv2.ml.ROW_SAMPLE, responses)

out = np.zeros(image.shape, np.uint8)

_, contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt):
        [x, y, w, h] = cv2.boundingRect(cnt)
        if h:
            cv2.rectangle(image, (x, y), (x + w, y + h), 125, 1)
            roi = image[y:y + h, x:x + w]
            skeleton = skeletonize(roi)
            ready = scale(skeleton, dim)
            if fourthMethodOn:
                vector = fourthMethod(ready)
            else:
                vector = thirdMethod(ready, rec)
            vector = np.reshape(vector, (1, rec*rec))
            vector = np.float32(vector)
            ret, results, neighbours, dist = knn.findNearest(vector, 1)
            string = str(chr(results[0][0]))
            cv2.putText(out, string, (x, y + h), 0, 1, (255, 255, 255))

cv2.imshow('im', image)
cv2.imshow('out', out)
cv2.waitKey(0)

