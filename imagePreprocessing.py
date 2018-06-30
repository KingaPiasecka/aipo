import cv2
import numpy as np

#Przygotowanie wstepne obrazu

def preprocessing(img):

    #Zamiana do odcieni szarosci
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Normalizacja histogramu - Contrast Limited Adaptive Histogram Equalization
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(1,1))
    img = clahe.apply(img)

    #binaryzacja
    #th, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    th, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_BINARY)
    # erozja i dylatacja
    kernel = np.ones((1,1), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)

    #ewentualna dodatkowa filtracja
    img = cv2.GaussianBlur(img,(1,1),1)

    return img