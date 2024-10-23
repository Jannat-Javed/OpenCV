import cv2

# Initialize video capture
cap = cv2.VideoCapture('Kakashi vs Sasuke Taijutsu Naruto Shippuden.mp4')

delay = 30  # Initial delay (normal speed)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video Speed Control', frame)

    key = cv2.waitKey(delay) & 0xFF
    if key == ord('x'):  # Increase speed
        delay = max(1, delay - 5)
    elif key == ord('c'):  # Decrease speed
        delay += 5
    elif key == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()
