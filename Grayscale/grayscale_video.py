import cv2

# converting to grayscale
cap = cv2.VideoCapture('Kakashi vs Sasuke Taijutsu Naruto Shippuden.mp4')
 
while cap.isOpened():
    ret, frame = cap.read()
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()