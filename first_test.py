import cv2
import os
img = cv2.imread("SAM5987.jpg")

# Resize to fit within 800px
h, w = img.shape[:2]
scale = 1000 / max(h, w)
resized = cv2.resize(img, (int(w*scale), int(h*scale)))
inverted = 255 - resized

# Show
cv2.namedWindow("Inverted", cv2.WINDOW_NORMAL)
cv2.imshow("Inverted", inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()
