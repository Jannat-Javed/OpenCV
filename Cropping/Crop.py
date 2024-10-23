import cv2 

# Load an image from file
image = cv2.imread('timothee.jpg')

# Crop the image (startY:endY, startX:endX)
cropped_image = image[90:400, 200:400]

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
