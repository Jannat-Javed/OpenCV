import cv2
import matplotlib.pyplot as plt


# Load the image in color
img = cv2.imread('jungkook.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 # Display the grayscale image using matplotlib
plt.imshow(gray_img, cmap='gray')  # 'cmap=gray' ensures the image is displayed in grayscale
plt.axis('off')  # Turn off the axis
plt.title('Grayscale Image')
plt.show()

