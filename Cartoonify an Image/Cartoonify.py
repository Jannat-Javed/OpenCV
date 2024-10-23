import cv2

def cartoonify_image(img):
    # Convert image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to smoothen the image
    gray_blurred = cv2.medianBlur(gray, 5)
    
    # Detect edges using adaptive threshold
    edges = cv2.adaptiveThreshold(gray_blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # Apply bilateral filter to remove noise and keep edges sharp
    color = cv2.bilateralFilter(img, 9, 300, 300)
    
    # Combine edges with the color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

# Read an image
image = cv2.imread('jungkook.jpg')

# Get cartoonified image
cartoon_image = cartoonify_image(image)

# Display the result
cv2.imshow('Cartoon Image', cartoon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()