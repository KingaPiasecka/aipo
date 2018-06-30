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


def firstMethod(img):
    vector = []
    height, width = img.shape
    for i in range(0, height):
        for j in range(0, width):
            if img[i, j] == 255:
                neighbours = surrounding(img, i, j)
                if neighbours != 2 and neighbours > 0:
                    vector.append([i, j])

    top = check_top(img)
    print top
    bottom = check_bottom(img)
    print bottom
    left_side = check_left_side(img)
    print left_side
    right_side = check_right_side(img)
    print right_side
    vector.extend(top)
    vector.extend(bottom)
    vector.extend(left_side)
    vector.extend(right_side)

    return vector


def surrounding(area, x, y):
    neighbours = []
    height, width = area.shape
    for i in range(x - 1 if x > 0 else x, x + 2 if x < height-1 else x+1):
        for j in range(y - 1 if y > 0 else y, y + 2 if y < width-1 else y+1):
            neighbours.append(area[i][j])
    return neighbours.count(255)-1


def check_top(img):
    vector = []
    points = []
    height, width = img.shape
    first_black = False
    for i in range(0, height):
        for j in range(0, width):
            if img[i, j] == 255:
                first_black = True
                vector.append([i, j])
        if first_black:
            if len(vector) == 1:
                return vector
            else:
                suma = vector[0][1]
                number = 1
                for p in range(1, len(vector)):
                    previous = vector[p-1]
                    current = vector[p]
                    if adjacent_points(previous[1], current[1]):
                        suma = suma + current[1]
                        number = number + 1
                    else:
                        average = suma / number
                        points.append([i, average])
                        suma = current[1]
                        number = 1

                average = suma / number
                points.append([i, average])
                break
    return points


def check_bottom(img):
    vector = []
    points = []
    height, width = img.shape
    first_black = False
    for i in range(height-1, -1, -1):
        for j in range(0, width):
            if img[i, j] == 255:
                first_black = True
                vector.append([i, j])
        if first_black:
            if len(vector) == 1:
                return vector
            else:
                suma = vector[0][1]
                number = 1
                for p in range(1, len(vector)):
                    previous = vector[p-1]
                    current = vector[p]
                    if adjacent_points(previous[1], current[1]):
                        suma = suma + current[1]
                        number = number + 1
                    else:
                        average = suma / number
                        points.append([i, average])
                        suma = current[1]
                        number = 1

                average = suma / number
                points.append([i, average])
                return points
    return points


def check_left_side(img):
    vector = []
    points = []
    height, width = img.shape
    first_black = False
    for j in range(0, width):
        for i in range(0, height):
            if img[i, j] == 255:
                first_black = True
                vector.append([i, j])
        if first_black:
            if len(vector) == 1:
                return vector
            else:
                suma = vector[0][0]
                number = 1
                for p in range(1, len(vector)):
                    previous = vector[p-1]
                    current = vector[p]
                    if adjacent_points(previous[0], current[0]):
                        suma = suma + current[0]
                        number = number + 1
                    else:
                        average = suma / number
                        points.append([average, j])
                        suma = current[0]
                        number = 1

                average = suma / number
                points.append([average, j])
                break
    return points


def check_right_side(img):
    vector = []
    points = []
    height, width = img.shape
    first_black = False
    for j in range(width-1, -1, -1):
        for i in range(0, height):
            if img[i, j] == 255:
                first_black = True
                vector.append([i, j])
        if first_black:
            if len(vector) == 1:
                return vector
            else:
                suma = vector[0][0]
                number = 1
                for p in range(1, len(vector)):
                    previous = vector[p-1]
                    current = vector[p]
                    if adjacent_points(previous[0], current[0]):
                        suma = suma + current[0]
                        number = number + 1
                    else:
                        average = suma / number
                        points.append([average, j])
                        suma = current[0]
                        number = 1

                average = suma / number
                points.append([average, j])
                break
    return points


def adjacent_points(point1, point2):
    return (point1-1 == point2) or (point2-1 == point1)


def fourthMethod(img):
    roi = cv2.resize(img, (10, 10))
    return roi.reshape((1, 100))