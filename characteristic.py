import cv2
import numpy as np

def secondMethod(image):

    w, h = image.shape[:2]
    vector = set()
    newImg = np.full((w, h), 255, np.uint8)
    cv2.line(newImg, (0, 0), (w, h-1), 0)
    cv2.line(newImg, (h, 0), (0, w-1), 0)
    cv2.line(newImg, (w//2, 0), (w//2, h-1), 0)
    cv2.line(newImg, (0, h//2), (w-1, h//2), 0)
    image = image + newImg

    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if pixel == 0:
                vector.add((i, j))

    return list(vector)


def thirdMethod(img,rect):
    vector = []
    w, h = img.shape[:2]

    rectW, rectH = int(w / rect), int(h / rect)

    for x in range(rect):
        for y in range(rect):
            count = 0
            for i in range(x * rectW, x * rectW + rectW):
                for j in range(y * rectH, y * rectH + rectH):
                    if img[i, j] == 255:
                        count += 1
            vector.append(np.float32(count))

    return vector
