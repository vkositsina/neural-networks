import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height

while True and cap.isOpened():
    buf = cap.read()
    ret = buf[0]
    if ret:
        frame = buf[1]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

        cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
