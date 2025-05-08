import cv2
import matplotlib.pyplot as plt

img = '../image1.png'

# Apply Gaussian filter
gaussian_filtered = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=0)
# Display original and filtered images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Gaussian Filtered')
plt.imshow(gaussian_filtered, cmap='gray')
plt.show()
