import cv2
import numpy as np
import matplotlib.pyplot as plt

def shadow(image_path, shadow_offset=(10, 10), blur_ksize=(21, 21), shadow_color=(0, 0, 0, 10)):
    # read the image with alpha channel
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    plt.title("Original Image")
    plt.imshow(image)
    plt.show()

    if image.shape[2] != 4:
        raise ValueError("Image must have an alpha channel")

    h, w = image.shape[:2]

    # Create shadow base from alpha channel
    alpha = image[:, :, 3]
    shadow = np.zeros((h, w, 4), dtype=np.uint8)
    shadow[:, :, :3] = shadow_color[:3]
    shadow[:, :, 3] = alpha

    # Apply Gaussian blur to the shadow
    blurred_shadow = cv2.GaussianBlur(shadow, blur_ksize, 0)

    # Create a larger canvas to accommodate the shadow offset
    canvas_h = h + shadow_offset[1]
    canvas_w = w + shadow_offset[0]
    canvas = np.zeros((canvas_h, canvas_w, 4), dtype=np.uint8)

    # Print the blurred iamge
    canvas[shadow_offset[1]:shadow_offset[1]+h, shadow_offset[0]:shadow_offset[0]+w] = blurred_shadow

    # Overlay original image onto the canvas
    canvas[0:h, 0:w] = overlay_image_alpha(canvas[0:h, 0:w], image)

    return canvas

def overlay_image_alpha(background, foreground):
    alpha = foreground[:, :, 3] / 255.0
    for c in range(3):
        background[:, :, c] = (1 - alpha) * background[:, :, c] + alpha * foreground[:, :, c]
    background[:, :, 3] = np.clip(foreground[:, :, 3] + background[:, :, 3] * (1 - alpha), 0, 255)
    return background.astype(np.uint8)


result = shadow("../image1.png", shadow_offset=(10, 10), blur_ksize=(21, 21), shadow_color=(0, 0, 0, 10))
plt.title("Shadow Effect")
plt.imshow(result)
plt.show()
