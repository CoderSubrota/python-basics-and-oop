import cv2

# Open the default webcam (0 refers to the first camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:
        # Capture each frame
        readCam, frame = cap.read()

        # If the frame was captured successfully, display it
        if readCam:
            cv2.imshow('Webcam Feed', frame)
        else:
            print("Error: Failed to capture frame.")
            break
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
