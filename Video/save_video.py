import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object with proper file extension
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Flip the video
    frame = cv2.flip(frame, 0)
    
    # Write the flipped frame
    out.write(frame)
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release everything if the job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
