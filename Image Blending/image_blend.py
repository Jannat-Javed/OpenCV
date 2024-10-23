import cv2

# Load images
img1 = cv2.imread('jungkook.jpg')
img2 = cv2.imread('timothee.jpg')


# Print shapes of the images
print(f"img1 shape: {img1.shape}")
print(f"img2 shape: {img2.shape}")

# Resize img2 to match img1's dimensions if necessary
if img1.shape[:2] != img2.shape[:2]:  # Check if height and width are different
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Blend the images
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# Display the blended image
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()