import skimage as sk
import matplotlib.pyplot as plt

image = sk.io.imread("../image.png", sk.color.rgb2gray)
plt.imshow(image)
plt.title('Original Image')
plt.show()


edges = sk.filters.sobel(image)

plt.imshow(edges, cmap='gray')
plt.title('Sobel Filtered Image')
plt.show()
