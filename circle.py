import cv2
from cv2 import circle
import numpy as np
import math

def find_contours(img, color):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(img_hsv, color[0], color[1])
    contours, _ = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

img = cv2.imread('img/pool_two_bins.jpg')
drawing = img.copy()
color = (
    (30, 80, 0),
    (70, 200, 255)
)

contours = find_contours(img, color)

for cnt in contours:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 100:
        cv2.drawContours(drawing, [cnt], 0, (255, 255, 255), 2)
        print("Площадь контура:", contour_area)

        # описанная окружность
        (circle_x, circle_y), circle_radius = cv2.minEnclosingCircle(cnt)
        cv2.circle(drawing, (int(circle_x), int(circle_y)), int(circle_radius), (255, 255, 0), 2)
        circle_area = math.pi * circle_radius ** 2
        print('Площадь круга:', circle_area)
        print()

cv2.imshow('drawing', drawing)
cv2.waitKey(0)