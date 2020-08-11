import cv2
import dlib
import os
import time
import sqlite3

cam = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
date = time.strftime("%d.%m.%Y")
path = './pics_taken/' + date
if not os.path.exists(path):
    os.makedirs(path)


def getProfile(id):
    connect = sqlite3.connect("Face-DataBase3")
    cmd = "SELECT * FROM Students WHERE ID=" + str(id)
    cursor = connect.execute(cmd)
    connect.execute("UPDATE Students SET Presents =Presents+1  WHERE ID = ?  AND LastUpdatedTime < date('now', '-1 hours')",str(id))
    connect.commit()
    profile = None
    for row in cursor:
        profile = row
        
    connect.close()
    return profile

rec = cv2.face.LBPHFaceRecognizer_create()                                          # Local Binary Patterns Histograms
rec.read('./recognizer/trainingData.yml')                                       # loading the trained data
               # the font of text on face recognition
font = cv2.FONT_HERSHEY_SIMPLEX
# make an array of all the students in the database initialied as zero

picNum = 1
while(True):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # conveting the camera input into GrayScale
    dets = detector(img, 1)
    
    totalConf = 0.0
    faceRec = 0
    for i, d in enumerate(dets):
        # picName = str(i + 1) + '.jpg'
        # picFolderName = folderName + '/' + picName
        id, conf = rec.predict(gray[d.top():d.bottom(), d.left():d.right()])    # Comparing from the trained data
        if conf < 150:
            totalConf += conf
            faceRec += 1
            profile = getProfile(id)
        cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (255, 255, 255), 2)
    cv2.imshow('frame', img)                                                     # Showing each frame on the window
    cv2.imwrite(path + '/pic' + str(picNum) + '.jpg', img)
    detectPrint = 'Frame' + str(picNum) + ". %d face detected" % len(dets)
    if faceRec != 0:
        print (detectPrint + " and ", faceRec, " face recognized with confidence %.2f"%(totalConf / faceRec))
    else:
        print (detectPrint + " and 0 faces recognized")
    picNum += 1
    k = cv2.waitKey(10) & 0xff                                                  # Turn off the recognizer using Esc Key
    if k == 27:
        break

cam.release()                                                                   # turning the webcam off
cv2.destroyAllWindows()                                                         # Closing all the opened windows
