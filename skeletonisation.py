import numpy as np
import scipy.ndimage.morphology as m
from skimage import morphology

def skeletonize(img):
    h1 = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 1]], dtype=np.uint8)
    m1 = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]], dtype=np.uint8)
    h2 = np.array([[0, 0, 0], [1, 1, 0], [0, 1, 0]], dtype=np.uint8)
    m2 = np.array([[0, 1, 1], [0, 0, 1], [0, 0, 0]], dtype=np.uint8)
    hit_list = []
    miss_list = []
    for k in range(4):
        hit_list.append(np.rot90(h1, k))
        hit_list.append(np.rot90(h2, k))
        miss_list.append(np.rot90(m1, k))
        miss_list.append(np.rot90(m2, k))
    img = img.copy()
    while True:
        last = img
        for hit, miss in zip(hit_list, miss_list):
            hm = m.binary_hit_or_miss(img, hit, miss)
            img = np.logical_and(img, np.logical_not(hm))
        if np.all(img == last):
            break

    img = img.astype(np.uint8) * 255
    out = morphology.skeletonize(img > 0)
    return img
