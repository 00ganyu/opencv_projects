import cv2
import numpy as np

# Read image
resize = cv2.imread("SAM5987.JPG")

img = cv2.resize(resize, (500,500))

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)

# Warp the Hue channel with a sine curve for psychedelic effect
h, s, v = cv2.split(hsv)
h = (h + 90*np.sin(h/20.0)).clip(0, 179)   # OpenCV hue range: [0,179]

# Boost saturation & invert value channel partly
s = np.clip(s*1.5, 0, 255)
v = 255 - v*0.7

# Merge back
hsv_warped = cv2.merge([h, s, v]).astype(np.uint8)
output = cv2.cvtColor(hsv_warped, cv2.COLOR_HSV2BGR)

# Optional: blend with original
final = cv2.addWeighted(img, 0.4, output, 0.6, 0)

cv2.imshow("Trippy Effect", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
