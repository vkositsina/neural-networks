import cv2

cap = cv2.VideoCapture(0)

while True and cap.isOpened():
    buf = cap.read()
    ret = buf[0]
    if ret:
        frame = buf[1]
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
