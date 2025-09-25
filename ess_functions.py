import cv2 as cv

img = cv.imread('SAM_7578.JPG')
h, w = img.shape[:2]
scale = 1000 / max(h, w)
resized = cv.resize(img, (int(w*scale), int(h*scale)))

# 1. converting img to gray scale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

# 2. blur
blur = cv.GaussianBlur(resized, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blurrrr', blur)

# 3. Edge Cascade
canny = cv.Canny(resized, 125,175)
cv.imshow('edge', canny)

# 4. dilate the image
dilated = cv.dilate(canny, (7,7), iterations= 4)
cv.imshow('dilated', dilated)

# 5. eroding
eroded = cv.erode(dilated, (7,7), iterations= 4)
cv.imshow('erode', eroded)

# 6. resize 
dawg = cv.imread('SAM_7586.JPG')
resize = cv.resize(dawg, (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('crop', resize)

# 7. cropping
cropped = dawg[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)
