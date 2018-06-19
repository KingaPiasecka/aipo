import cv2


def segment_and_scale(image):
    """
    :rtype: collections.list
    """
    im = image
    _, contours, _ = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    characters = []
    for cnt in contours:
        if cv2.contourArea(cnt):
            [x, y, w, h] = cv2.boundingRect(cnt)

            if h:
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
                roi = im[y:y + h, x:x + w]
                roismall = cv2.resize(roi, (10, 10))
                characters.append(roi)

    return characters
