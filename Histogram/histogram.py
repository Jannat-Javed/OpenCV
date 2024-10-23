import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('jungkook.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Display the original grayscale image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Display the histogram
plt.subplot(1, 2, 2)
plt.plot(hist, color='black')
plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Show the plots
plt.tight_layout()
plt.show()