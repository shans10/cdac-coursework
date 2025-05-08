import skimage as sk
import matplotlib.pyplot as plt
import numpy as np

image = sk.io.imread('../image.png', sk.color.rgb2gray)
plt.imshow(image)
plt.title('Original Image')
plt.show()

harris = sk.feature.corner_harris(image)
corners = sk.feature.corner_peaks(harris, min_distance=2, threshold_rel=0.02)

corner_image = np.zeros_like(image)
corner_image[corners[:, 0], corners[:, 1]] = 1

plt.imshow(corner_image, cmap='gray')
plt.title('Harris Corners')
plt.show()
