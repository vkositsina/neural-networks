''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc

Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18

'''

import cv2
import os

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('./video_for_traine/ПрутскийTrim.mp4')
#cap = cv2.VideoCapture('./video_for_traine/НавальныйTrim.mp4')
# cap = cv2.VideoCapture('./video_for_traine/ПутинTrim.mp4')
cap.set(3, 640)  # set video width
cap.set(4, 480)  # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface.xml')

# For each person, enter one numeric face id
face_id = input('Enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while True and cap.isOpened():
    buf = cap.read()
    ret = buf[0]
    if ret:
        frame = buf[1]
        # cv2.imshow('frame', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])


    k = cv2.waitKey(30) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 60:  # Take 30 face sample and stop video
        break


# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cap.release()
cv2.destroyAllWindows()
