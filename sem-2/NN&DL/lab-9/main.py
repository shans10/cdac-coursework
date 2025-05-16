import numpy as np

# a. Sample 5x5 grayscale image (values from 0 to 255)
image = np.array(
    [
        [10, 50, 80, 60, 20],
        [30, 100, 200, 150, 30],
        [50, 120, 255, 180, 40],
        [20, 90, 160, 140, 20],
        [10, 60, 70, 50, 10],
    ]
)

# b. Example 3x3 kernel (edge detector / sharpening filter)
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])


def convolve2d(image, kernel):
    """Manual 2D convolution without padding"""
    image_h, image_w = image.shape
    kernel_h, kernel_w = kernel.shape
    output_h = image_h - kernel_h + 1
    output_w = image_w - kernel_w + 1

    output = np.zeros((output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            region = image[i : i + kernel_h, j : j + kernel_w]
            output[i, j] = np.sum(region * kernel)

    return output


# Perform convolution
convolved = convolve2d(image, kernel)

# Display results
print("Original Image:\n", image)
print("\nKernel:\n", kernel)
print("\nConvolved Output:\n", convolved.astype(int))
