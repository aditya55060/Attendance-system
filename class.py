'''import cv2
wCam,hCam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while(True):
    success, img =cap.read()
    cv2.imshow("Web cam", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()'''




'''import cv2
wCam,hCam = 352,288

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
#load background
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

startY = 96
startX = 36

while(True):
    success, img =cap.read()
    #..........................
    imgBackground[startY: startY+hCam , startX:startX+wCam] = img

    cv2.imshow("Web cam", img)
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''

'''import cv2
import os
wCam,hCam = 352,288

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
#load background
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

startY = 96
startX = 36

#................
folderModePath = "D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\modes"
modePathList = os.listdir(folderModePath)
imgModeList = []
#D:\Course_Material\Opencv\CvAttendance_System\Resources\modes\1.png
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imgModeList.append(img)

print(imgModeList, len(imgModeList))

#.............

while(True):
    success, img =cap.read()
    imgBackground[startY: startY+hCam , startX:startX+wCam] = img
    
    #cv2.imshow("Web cam", img)
    #cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
'''import cv2
import os
wCam,hCam = 352,288

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
#load background
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

startY = 96
startX = 36

folderModePath = "D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\modes"
modePathList = os.listdir(folderModePath)
imgModeList = []
#D:\Course_Material\Opencv\CvAttendance_System\Resources\modes\1.png
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imgModeList.append(img)

print(imgModeList, len(imgModeList))


while(True):
    success, img =cap.read()
    imgBackground[startY: startY+hCam , startX:startX+wCam] = img

    #....................
    h,w,c =imgModeList[1].shape

    imgBackground[30: 30+h, 450: 450+w] = imgModeList[1]
    #....................
    
    #cv2.imshow("Web cam", img)
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''

'''import cv2
import os
#..........
import face_recognition
#.........
import pickle


wCam,hCam = 352,288

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
#load background
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

startY = 96
startX = 36

folderModePath = "D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\modes"
modePathList = os.listdir(folderModePath)
imgModeList = []
#D:\Course_Material\Opencv\CvAttendance_System\Resources\modes\1.png
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imgModeList.append(img)

print(imgModeList, len(imgModeList))

#....................
print("Loading Encoding File....")
file = open("D:\\Course_Material\\Opencv\\CvAttendance_System\\EncodeFile.p","rb")
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Encoded file loaded....")
#....................

while(True):
    success, img =cap.read()
    #...............
    imgS = cv2.resize(img, (0,0),None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    #..................

    imgBackground[startY: startY+hCam , startX:startX+wCam] = img


    
    h,w,c =imgModeList[1].shape

    imgBackground[30: 30+h, 450: 450+w] = imgModeList[1]
    #.....................
    #find the location in current frame
    faceCurFrame= face_recognition.face_locations(imgS)

    #..encode face in current frame
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame )

    for encodeFace,faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print("matches ",matches)
        print("Face Dist", faceDis)




    #.....................
  
    
    #cv2.imshow("Web cam", img)
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''


import cv2
import os
#..........
import face_recognition
#.........
import pickle
import numpy as np


wCam,hCam = 352,288

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
#load background
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

startY = 96
startX = 36

folderModePath = "D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\modes"
modePathList = os.listdir(folderModePath)
imgModeList = []
#D:\Course_Material\Opencv\CvAttendance_System\Resources\modes\1.png
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imgModeList.append(img)

print(imgModeList, len(imgModeList))

#....................
print("Loading Encoding File....")
file = open("D:\\Course_Material\\Opencv\\CvAttendance_System\\EncodeFile.p","rb")
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Encoded file loaded....")
#....................

while(True):
    success, img =cap.read()
   
    imgS = cv2.resize(img, (0,0),None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 

    imgBackground[startY: startY+hCam , startX:startX+wCam] = img


    
    h,w,c =imgModeList[1].shape

    imgBackground[30: 30+h, 450: 450+w] = imgModeList[1]
  
    #find the location in current frame
    faceCurFrame= face_recognition.face_locations(imgS)

    #..encode face in current frame
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame )

    for encodeFace,faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print("matches ",matches)
        print("Face Dist", faceDis)

        #................
        matchIndex = np.argmin(faceDis)
        print("matchIndex: ",matchIndex)

        if(matches[ matchIndex]):
            print("Known detected")
            print(studentIds[matchIndex])



        #.....................




  
  
    
    #cv2.imshow("Web cam", img)
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()











