import numpy as np
import scipy.ndimage.morphology as m
import cv2

def skeletonize(img):
    # h1 = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]], dtype=np.uint8)
    # m1 = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]], dtype=np.uint8)
    # h2 = np.array([[0, 0, 0], [1, 1, 0], [0, 1, 0]], dtype=np.uint8)
    # m2 = np.array([[0, 1, 1], [0, 0, 1], [0, 0, 0]], dtype=np.uint8)
    # hit_list = []
    # miss_list = []
    # for k in range(4):
    #     hit_list.append(np.rot90(h1, k))
    #     hit_list.append(np.rot90(h2, k))
    #     miss_list.append(np.rot90(m1, k))
    #     miss_list.append(np.rot90(m2, k))
    # img = img.copy()
    # while True:
    #     last = img
    #     for hit, miss in zip(hit_list, miss_list):
    #         hm = m.binary_hit_or_miss(img, hit, miss)
    #         img = np.logical_and(img, np.logical_not(hm))
    #     if np.all(img == last):
    #         break
    #
    # img = img.astype(np.uint8) * 255
    # return img

    ##############################

    # img = img.copy()
    #
    # size = np.size(img)
    # skel = np.zeros(img.shape, np.uint8)
    #
    # ret, img = cv2.threshold(img, 127, 255, 0)
    # element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    # done = False
    #
    # while not done:
    #     eroded = cv2.erode(img, element)
    #     temp = cv2.dilate(eroded, element)
    #     temp = cv2.subtract(img, temp)
    #     skel = cv2.bitwise_or(skel, temp)
    #     img = eroded.copy()
    #
    #     zeros = size - cv2.countNonZero(img)
    #     if zeros == size:
    #         done = True
    #
    # return skel
    img = img.copy()
    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)
    ret, img = cv2.threshold(img, 127, 255, 0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while (not done):
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True

    return skel
