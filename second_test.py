import cv2
import matplotlib.pyplot as plt
'''
img = cv2.imread("SAM5987.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
inverted = 255 - img_rgb
plt.imshow(inverted)
plt.title("Inverted Image")
plt.axis("off")
plt.show()
'''

img1 = cv2.imread("SAM_7578.jpg")
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img1_gray = cv2.cvtColor(img1_rgb, cv2.COLOR_RGB2GRAY)
h, w = img1_gray.shape[:2]
scale = 1000 / max(h, w)
resized = cv2.resize(img1_gray, (int(w*scale), int(h*scale)))
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows() 
'''
plt.imshow(img1_gray)~
plt.axis("off")
plt.show()
'''