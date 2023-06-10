import cv2
from matplotlib import pyplot as plt

image = cv2.imread('riram.jpg',0)

img_sobelx = cv2.Sobel(image,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(image,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

fig, axes = plt.subplots(4, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(image, cmap ='gray')
ax[0].set_title("Citra Input")
ax[1].hist(image.ravel(), bins = 256)
ax[1].set_title("Histogram Citra Input")

ax[2].imshow(img_sobelx, cmap ='gray')
ax[2].set_title("Citra Input")
ax[3].hist(img_sobelx.ravel(), bins = 256)
ax[3].set_title("Histogram Citra Input")

ax[4].imshow(img_sobely, cmap ='gray')
ax[4].set_title("Citra Input")
ax[5].hist(img_sobely.ravel(), bins = 256)
ax[5].set_title("Histogram Citra Input")

ax[6].imshow(img_sobel, cmap ='gray')
ax[6].set_title("Citra Input")
ax[7].hist(img_sobel.ravel(), bins = 256)
ax[7].set_title("Histogram Citra Input")

fig.tight_layout()
plt.show()