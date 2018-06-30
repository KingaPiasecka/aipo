import cv2
import numpy as np

def rotate(image):

  # minAreaRect on the nozeros
    pts = cv2.findNonZero(image)
    ret = cv2.minAreaRect(pts)

    (cx, cy), (w, h), ang = ret
    if w > h:
        w, h = h, w
        ang += 90

    # Find rotated matrix, do rotation
    M = cv2.getRotationMatrix2D((cx, cy), ang, 1.0)
    rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return rotated


def rotate2(img):
    # wyrownywanie (rotacja) obrazu
    coords = np.column_stack(np.where(img > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    print("[INFO] angle: {:.3f}".format(angle))
    return img