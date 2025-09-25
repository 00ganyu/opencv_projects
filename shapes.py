# can draw images
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('blanks', blank)
#img = cv.imread('SAM_7586.JPG')
#cv.imshow('image', img)

#1. paint the image in certain color
#blank[:] = 0,255,0 #BGR CHANNELS. 255 IS FULL VALUE FOR GREEN IN 8BIT

#blank[200:300, 300:400] = 0,255,0
#cv.imshow('green', blank)

# 2. draw rectangle
#cv.rectangle(blank, (0,20), (100,250), (0,250,0), thickness = 2)
#thickness = cv.FILLED or -1 fills rectangle
cv.rectangle(blank, (0,20), (blank.shape[1]//2, blank.shape[0]//2) ,(0,250,0), thickness = -1)
cv.imshow('rectangle', blank)
#3. draw a circle
cv.circle(blank, (250,250), 40, (0,100,250), thickness = -1)
cv.imshow('circle', blank)

#4. draw a line
cv.line(blank, (499,499), (0,0), (120,90,0), thickness = 5)
cv.line(blank, (499,0), (0,499), (120,90,0), thickness = 5)
cv.line(blank, (499,250), (0,250), (120,90,0), thickness = 5)
cv.line(blank, (250,499), (250,0), (120,90,0), thickness = 5)
cv.imshow('line', blank)
cv.waitKey(0)
