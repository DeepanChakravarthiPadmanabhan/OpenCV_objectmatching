import numpy as np
import cv2
import matplotlib.pyplot as plt
f, axs = plt.subplots(2,2,figsize=(15,6))
BLACK_THRESHOLD = 200
THIN_THRESHOLD = 10

im = cv2.imread('/home/deepan/PycharmProjects/techchallenge/image_tech/Q3.jpeg')
im = cv2.GaussianBlur(im,(5,5),0)
im = cv2.Canny(im,120,500)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# cv2.imshow("input_img", im)
# cv2.waitKey()
ret, thresh = cv2.threshold(imgray, 130,55 , 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(im,contours,-1,(0,255,0),3)
cv2.imshow("window title", im)
idx = 0
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
contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
objects = np.zeros([self.image.shape[0],self.image.shape[1], 'uint8')
self.center_points = []
for c in contours:
    area = cv2.contourArea(c)
    if area >= 1 and area <= 100000:
        cv2.drawContours(objects,[c],-1,(255,0,0),-1)
        M = cv2.moments(c)
        cx = int( M['m10']/M['m00'])
        cy = int( M['m01']/M['m00'])
        self.center_points.append((cx,cy))
        cv2.circle(objects,(cx,cy),4,(0,0,255),-1)
if self.save == True:
    cv2.imwrite('cavitycontours.jpg',objects)
if show == True or self.show == True:
        self.show_image(objects,"Extracted Contours")