import cv2

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