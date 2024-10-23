import cv2

def sketch(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Gaussian Blur
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Extract edges
    edges = cv2.Canny(blurred_image, 10, 70)
    
    # Invert binary image
    ret, mask = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

# Initialize webcam capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Get the sketch effect
    sketch_frame = sketch(frame)
    
    # Display the sketch
    cv2.imshow('Live Sketch', sketch_frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()