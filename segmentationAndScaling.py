import cv2


def segment(image):
    """
    :rtype: collections.list
    """
    im = image
    _, contours, _ = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    characters = []
    for cnt in contours:
        if cv2.contourArea(cnt) > 50:
            [x, y, w, h] = cv2.boundingRect(cnt)
            if h:
                cv2.rectangle(image, (x, y), (x + w, y + h), 125, 1)
                roi = image[y:y + h, x:x + w]
                characters.append(roi)

    return image, characters


def scale(image, dim):
    roismall = cv2.resize(image, (dim, dim))
    return  roismall