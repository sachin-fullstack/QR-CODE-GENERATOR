import cv2
from pyzbar.pyzbar import decode

# create a VideoCapture object to capture video from the default camera
cap = cv2.VideoCapture(0)

while True:
    # read a frame from the video stream
    ret, frame = cap.read()

    # decode any QR codes in the frame
    decoded_objs = decode(frame)

    # loop over the decoded objects
    for obj in decoded_objs:
        # print the type and data of the QR code
        print(f"Type: {obj.type}, Data: {obj.data}")

    # display the frame with any QR codes highlighted
    cv2.imshow("QR Code Scanner", frame)

    # wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, break from the loop
    if key == ord('q'):
        break

# release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
