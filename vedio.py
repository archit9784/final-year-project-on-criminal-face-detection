import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from plyer import notification
from PIL import ImageGrab

path = '/Users/dhakad/Downloads/Face-Recognition-master/ImagesBasic'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print("archit")
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


# def markAttendance(name):
#     with open('Attendance.csv', 'a+') as f:
#         try:
#             f.seek(0)  # Move cursor to the beginning of the file
#             myDataList = f.readlines()
#             now = datetime.now()
#             dtString = now.strftime('%Y-%m-%d,%H:%M:%S')  # Include date in the format YYYY-MM-DD
#
#             # Write attendance record for every appearance
#             f.write(f'\n{name},{dtString}')
#             print(f'{name} marked attendance at {dtString}')
#
#             notification_title = "Intruder Detected"
#             notification_message = f"Intruder detected: {name}. Be alert!"
#             notification_timeout = 5  # Notification will disappear after 5 seconds
#             notification.notify(
#                 title=notification_title,
#                 message=notification_message,
#                 timeout=notification_timeout
#             )
#         except Exception as e:
#             print(f'Error: {e}')



# 20 sec interval

from collections import defaultdict

# Dictionary to store the last attendance time for each individual
last_attendance_time = defaultdict(lambda: datetime.min)

def markAttendance(name):
    global last_attendance_time
    with open('Attendance.csv', 'a+') as f:
        try:
            now = datetime.now()
            dtString = now.strftime('%Y-%m-%d,%H:%M:%S')  # Include date in the format YYYY-MM-DD

            # Check if 20 seconds have passed since the last attendance for this individual
            last_marked_time = last_attendance_time[name]
            if (now - last_marked_time).total_seconds() >= 20:
                f.write(f'\n{name},{dtString}')
                print(f'{name} marked attendance at {dtString}')

                notification_title = "Intruder Detected"
                notification_message = f"Intruder detected: {name}. Be alert!"
                notification_timeout = 5  # Notification will disappear after 5 seconds
                notification.notify(
                    title=notification_title,
                    message=notification_message,
                    timeout=notification_timeout
                )

                # Update the last attendance time for this individual
                last_attendance_time[name] = now
            else:
                print(f'Attendance for {name} already marked recently.')
        except Exception as e:
            print(f'Error: {e}')





# FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))\


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            markAttendance(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
