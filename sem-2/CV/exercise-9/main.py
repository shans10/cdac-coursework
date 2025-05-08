import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_gaussian_pyramid(image, levels=3):
    pyramid = [image]
    for i in range(levels - 1):
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(pyramid[i], (5, 5), 1)
        # Downsample the image
        downsampled = cv2.pyrDown(blurred)
        pyramid.append(downsampled)

    return pyramid

image = cv2.imread("../image.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create Gaussian Pyramid with 3 levels
pyramid = create_gaussian_pyramid(image_rgb, levels=3)

# Plot the images in the pyramid
plt.figure(figsize=(15, 5))

for i, img in enumerate(pyramid):
    plt.subplot(1, len(pyramid), i + 1)
    plt.title(f"Level {i + 1}")
    plt.imshow(img)
plt.tight_layout()
plt.show()
