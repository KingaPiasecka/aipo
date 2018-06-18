import cv2


def segment_and_scale(image):
    # type: (string) -> str
    """

    :rtype: collections.list
    """
    im = cv2.imread(image)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('thresh', thresh)
    characters = []
    for cnt in contours:
        if cv2.contourArea(cnt):
            [x, y, w, h] = cv2.boundingRect(cnt)

            if h:
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
                roi = thresh[y:y + h, x:x + w]
                roismall = cv2.resize(roi, (10, 10))
                characters.append(roi)

    return characters
