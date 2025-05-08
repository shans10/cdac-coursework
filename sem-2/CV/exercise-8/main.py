import cv2
import matplotlib.pyplot as plt

img = '../image1.png'

# Apply Laplacian filter
laplacian_filtered = cv2.Laplacian(img, ddepth=cv2.CV_64F)
# Display original and filtered images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Laplacian Filtered')
plt.imshow(laplacian_filtered, cmap='gray')
plt.show()
