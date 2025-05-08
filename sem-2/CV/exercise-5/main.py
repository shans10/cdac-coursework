import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../image.png", cv2.IMREAD_GRAYSCALE)

# Apply box filter
box_filtered = cv2.boxFilter(img, ddepth=-1, ksize=(5, 5))

# Display original and filtered images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Box Filtered')
plt.imshow(box_filtered, cmap='gray')
plt.show()
