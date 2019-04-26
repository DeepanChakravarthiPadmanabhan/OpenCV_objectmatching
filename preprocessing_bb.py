import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_object(img):

    BLACK_THRESHOLD = 200
    THIN_THRESHOLD = 10

    img = cv2.GaussianBlur(img, (5, 5), 0)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(imgray, 130, 55, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    idx = 0
    for cnt in contours:
        idx += 1
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img[y:y + h, x:x + w]
        if h < THIN_THRESHOLD or w < THIN_THRESHOLD:
            continue
        # cv2.imwrite(str(idx) + '.png', roi)
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 0, 0), 2)

    return img

if __name__ == "__main__":


    img = cv2.imread('image_tech/Q3.jpeg')
    out = get_object(img)

    cv2.imshow('Output', out)
    cv2.waitKey()
