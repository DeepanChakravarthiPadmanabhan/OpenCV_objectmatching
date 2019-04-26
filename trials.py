import numpy as np
import cv2
import matplotlib.pyplot as plt
f, axs = plt.subplots(2,2,figsize=(15,6))
BLACK_THRESHOLD = 200
THIN_THRESHOLD = 10

im = cv2.imread('/home/deepan/PycharmProjects/techchallenge/image_tech/Q3.jpeg')
im = cv2.GaussianBlur(im,(5,5),0)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.Canny(th3,120,500)
# th3 = cv2.erode(th3, None, iterations=1)
contours, hierarchy = cv2.findContours(th3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("window title", im)
idx = 0
cv2.imshow('threshold',th3)
cv2.waitKey()
center_points = []
objects = np.zeros([im.shape[0],im.shape[1],3], 'uint8')
save=True
for c in contours:
    area = cv2.contourArea(c)
    if area >= 120 and area <= 100000:
        cv2.drawContours(objects,[c],-1,(255,0,0),-1)
        M = cv2.moments(c)
        cx = int( M['m10']/M['m00'])
        cy = int( M['m01']/M['m00'])
        center_points.append((cx,cy))
        cv2.circle(objects,(cx,cy),4,(0,0,255),-1)
if save == True:
    cv2.imwrite('cavitycontours.jpg',objects)
for cnt in contours:
    idx += 1
    x, y, w, h = cv2.boundingRect(cnt)
    roi = im[y:y + h, x:x + w]
    if h < THIN_THRESHOLD or w < THIN_THRESHOLD:
        continue
    # cv2.imwrite(str(idx) + '.png', roi)
    cv2.rectangle(im, (x, y), (x + w, y + h), (200, 0, 0), 2)
cv2.imshow('img', im)
cv2.waitKey()
