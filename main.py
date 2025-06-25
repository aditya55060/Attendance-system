#Check The camera 

'''import cv2
import time
import os


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while(True):
    success, img = cap.read()
    cv2.imshow("Web Cam",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()'''

#........fix camera in background image......
'''import cv2

# Set camera resolution
wCam, hCam = 352, 288

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # Width
cap.set(4, hCam)  # Height

# Load background image
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

# Get the dimensions of the background image
bgHeight, bgWidth, _ = imgBackground.shape

# Define placement dimensions
startY = 96  # Starting y-coordinate for placement
startX = 36  # Starting x-coordinate for placement

# Ensure the placement region fits within the background dimensions
if startY + hCam > bgHeight or startX + wCam > bgWidth:
    print(f"Error: Webcam image does not fit within the background dimensions.")
    cap.release()
    exit()

while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame from camera.")
        break

    # Overlay the webcam feed onto the background
    imgBackground[startY:startY + hCam, startX:startX + wCam] = img

    cv2.imshow("Web Cam", img)
    # Show the combined output
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()'''

#.........# Importing the mode images into a list

'''import cv2
import os

# Set camera resolution
wCam, hCam = 352, 288

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # Width
cap.set(4, hCam)  # Height

# Load background image
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

# Get the dimensions of the background image
bgHeight, bgWidth, _ = imgBackground.shape

# Define placement dimensions
startY = 96  # Starting y-coordinate for placement
startX = 36  # Starting x-coordinate for placement

# Ensure the placement region fits within the background dimensions
if startY + hCam > bgHeight or startX + wCam > bgWidth:
    print(f"Error: Webcam image does not fit within the background dimensions.")
    cap.release()
    exit()
#........................
# Importing the mode images into a list
folderModePath = 'D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imgModeList.append(img)
print(imgModeList,len(imgModeList))
#.........................

while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame from camera.")
        break

    # Overlay the webcam feed onto the background
    imgBackground[startY:startY + hCam, startX:startX + wCam] = img

    cv2.imshow("Web Cam", img)
    # Show the combined output
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()'''

#....check the modes pic fitting in background or not

'''import cv2
import os

# Set camera resolution
wCam, hCam = 352, 288

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # Width
cap.set(4, hCam)  # Height

# Load background image
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

# Get the dimensions of the background image
bgHeight, bgWidth, _ = imgBackground.shape


startY = 96
startX = 36
# Ensure the placement region fits within the background dimensions
if startY + hCam > bgHeight or startX + wCam > bgWidth:
    print(f"Error: Webcam image does not fit within the background dimensions.")
    cap.release()
    exit()
#........................
# Importing the mode images into a list
folderModePath = 'D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imgModeList.append(img)
#print(imgModeList,len(imgModeList))
#.........................

while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame from camera.")
        break

    # Overlay the webcam feed onto the background
    #width: 763 pixels
    #height: 427 pixels
    imgBackground[startY:startY + hCam, startX:startX + wCam] = img
    
    # Resize the mode image dynamically to fit the target region
    #modeImageResized = cv2.resize(imgModeList[1], (352, 330))  # Match width (352) and height (330)
    h,w,c = imgModeList[1].shape
    imgBackground[40:40 + h, 450:450 + w] = imgModeList[1]



    cv2.imshow("Web Cam", img)
    # Show the combined output
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
#...import Encoded file  and get Ids of students/user ....

'''import cv2
import os
#..........
import pickle
#...........

# Set camera resolution
wCam, hCam = 352, 288

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # Width
cap.set(4, hCam)  # Height

# Load background image
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

# Get the dimensions of the background image
bgHeight, bgWidth, _ = imgBackground.shape


startY = 96
startX = 36
# Ensure the placement region fits within the background dimensions
if startY + hCam > bgHeight or startX + wCam > bgWidth:
    print(f"Error: Webcam image does not fit within the background dimensions.")
    cap.release()
    exit()

# Importing the mode images into a list
folderModePath = 'D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imgModeList.append(img)
#print(imgModeList,len(imgModeList))

#.......................
print("Loading Encoding File...")
file = open("D:\\Course_Material\\Opencv\\CvAttendance_System\\EncodeFile.p","rb")

#What we have incoded that will get in this step
encodeListKnownWithIds = pickle.load(file)
file.close()

encodeListKnown, studentIds=encodeListKnownWithIds
print(studentIds)
print("Encoded File Loaded...")

#........................
while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame from camera.")
        break

    # Overlay the webcam feed onto the background
    #width: 763 pixels
    #height: 427 pixels
    imgBackground[startY:startY + hCam, startX:startX + wCam] = img
    
    # Resize the mode image dynamically to fit the target region
    #modeImageResized = cv2.resize(imgModeList[1], (352, 330))  # Match width (352) and height (330)
    h,w,c = imgModeList[1].shape
    imgBackground[40:40 + h, 450:450 + w] = imgModeList[1]



    cv2.imshow("Web Cam", img)
    # Show the combined output
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''


#.................Check if faces match or not  with webcam image......




import cv2
import os

import pickle

#................
import face_recognition
#...............


# Set camera resolution
wCam, hCam = 352, 288

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # Width
cap.set(4, hCam)  # Height

# Load background image
imgBackground = cv2.imread("D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\background.png")

# Get the dimensions of the background image
bgHeight, bgWidth, _ = imgBackground.shape


startY = 96
startX = 36
# Ensure the placement region fits within the background dimensions
if startY + hCam > bgHeight or startX + wCam > bgWidth:
    print(f"Error: Webcam image does not fit within the background dimensions.")
    cap.release()
    exit()

# Importing the mode images into a list
folderModePath = 'D:\\Course_Material\\Opencv\\CvAttendance_System\\Resources\\Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    imgModeList.append(img)
#print(imgModeList,len(imgModeList))

print("Loading Encoding File...")
file = open("D:\\Course_Material\\Opencv\\CvAttendance_System\\EncodeFile.p","rb")

#What we have incoded that will get in this step
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds=encodeListKnownWithIds
print(studentIds)
print("Encoding File Loaded...")


while True:
    success, img = cap.read()

    #........................................
    # Resize the images by scale (%) , to reduce the processing power
    imgS = cv2.resize(img, (0,0),None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    #find the location in current frame
    faceCurFrame = face_recognition.face_locations(imgS)

    #now encode  this current face and compare  with previous encoded faces
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("matches", matches) #List of matched face(True/False)
        print("faceDis", faceDis)#Lower the face distance means better match

    #...........................................

    if not success:
        print("Failed to grab frame from camera.")
        break

    # Overlay the webcam feed onto the background
    #width: 763 pixels
    #height: 427 pixels
    imgBackground[startY:startY + hCam, startX:startX + wCam] = img
    
    # Resize the mode image dynamically to fit the target region
    #modeImageResized = cv2.resize(imgModeList[1], (352, 330))  # Match width (352) and height (330)
    h,w,c = imgModeList[1].shape
    imgBackground[40:40 + h, 450:450 + w] = imgModeList[1]



    cv2.imshow("Web Cam", img)
    # Show the combined output
    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
