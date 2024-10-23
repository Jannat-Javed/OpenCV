import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Step 1: Load the original image
img = cv.imread('jungkook.jpg')


# Convert the original image to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Step 2: Add artificial noise (salt and pepper noise)
noisy_img = img_gray.copy()
prob = 0.02  # Noise probability
noise = np.random.rand(*noisy_img.shape)
noisy_img[noise < prob] = 0  # Pepper noise
noisy_img[noise > 1 - prob] = 255  # Salt noise

# Ensure noisy_img is in the valid range [0, 255]
noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

# Step 3: Denoise the image using fastNlMeansDenoising
denoised_img = cv.fastNlMeansDenoising(noisy_img, None, 30, 7, 21)

# Step 4: Display results using Matplotlib
plt.figure(figsize=(12, 4))

# Convert images to RGB for display
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
noisy_img_rgb = cv.cvtColor(noisy_img, cv.COLOR_GRAY2RGB)
denoised_img_rgb = cv.cvtColor(denoised_img, cv.COLOR_GRAY2RGB)

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

# Noisy Image
plt.subplot(1, 3, 2)
plt.imshow(noisy_img, cmap='gray')  # Display grayscale images with cmap='gray'
plt.title('Noisy Image')
plt.axis('off')

# Denoised Image
plt.subplot(1, 3, 3)
plt.imshow(denoised_img, cmap='gray')  # Display grayscale images with cmap='gray'
plt.title('Denoised Image')
plt.axis('off')

plt.tight_layout()
plt.show()
