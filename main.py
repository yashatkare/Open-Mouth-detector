import cv2
import numpy as np

# Load Haar cascade for mouth detection
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mouth.xml')

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set desired width and height of the video frames
frame_width = 640
frame_height = 480
cap.set(3, frame_width)
cap.set(4, frame_height)

# Calculate the distance between the red dots for mouth opening detection
mouth_open_threshold = 3  # in centimeters
mouth_open_threshold_pixels = int(mouth_open_threshold * frame_width / 20)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale for mouth detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect mouths in the grayscale frame
    mouths = mouth_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in mouths:
        # Draw red dots on the edge of the detected mouth
        dot1 = (x + int(w / 2), y)
        dot2 = (x + int(w / 2), y + h)
        cv2.circle(frame, dot1, 5, (0, 0, 255), -1)
        cv2.circle(frame, dot2, 5, (0, 0, 255), -1)
        

        # Apply filter effect to differentiate when the mouth is opened wider than the threshold
        if w > mouth_open_threshold_pixels:
            cv2.putText(frame, "Mouth Opened", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Mouth Recognition", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
