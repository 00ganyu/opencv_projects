import cv2
import numpy as np
import random

Resize = cv2.imread("SAM5987.JPG")
img = cv2.resize(Resize, (1500,1000))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
h, s, v = cv2.split(hsv)

hue_shift  = random.randint(20, 179)   
hue_freq   = random.uniform(5, 60)      
sat_boost  = random.uniform(0.5, 2.5)   
val_invert = random.uniform(0.1, 1.0)   
     
h = (h + hue_shift * np.sin(h / hue_freq)).clip(0, 179)
s = np.clip(s * sat_boost, 0, 255)
v = 255 - v * val_invert

hsv_warped = cv2.merge([h, s, v]).astype(np.uint8)
out = cv2.cvtColor(hsv_warped, cv2.COLOR_HSV2BGR)
output = cv2.GaussianBlur(out, (3,3), cv2.BORDER_DEFAULT)

alpha = random.uniform(0.4, 0.7)  
final = cv2.addWeighted(img, 1 - alpha, output, alpha, 0)

cv2.imshow("Random Trippy Effect", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
