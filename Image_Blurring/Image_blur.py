import cv2

# Load the image
image = cv2.imread('timothee.jpg')

# Apply different types of blurring
blurred = cv2.blur(image, (5, 5))  # Average blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)  # Gaussian blur
median_blur = cv2.medianBlur(image, 5)  # Median blur
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)  # Bilateral filter

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Filter', bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
