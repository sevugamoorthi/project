import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Calculate the absolute difference between the two frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Blur the image to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold the image
    _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill in holes
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours of the moving objects
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # If the contour is large enough, it is considered a moving object
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frames
    cv2.imshow("Frame", frame1)

    # Move to the next frames
    frame1 = frame2
    ret, frame2 = cap.read()

    # Break the loop if 'q' is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
