#Copied code from firebase & path of downloaded .json file renamed to 
#faceattendancekey.json
'''import firebase_admin #pip install firebase-admin

from firebase_admin import credentials

cred = credentials.Certificate("D:\\Course_Material\\Opencv\\CvAttendance_System\\faceattendancekey.json")
firebase_admin.initialize_app(cred)'''


# Now add the realtime data base url from realtime data base in firebase

'''import firebase_admin 
from firebase_admin import credentials

cred = credentials.Certificate("D:\\Course_Material\\Opencv\\CvAttendance_System\\firebaseKey.json")
firebase_admin.initialize_app(cred,{

'databaseURL':""


})
'''

#...Now Add the data in  the Realtime database ......
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("D:\\Course_Material\\Opencv\\CvAttendance_System\\firebaseKey.json")
firebase_admin.initialize_app(cred,{
    
'databaseURL':""


})
#...............
ref = db.reference("Students")
#Add data
data ={
    "123":
        {
            "Name": "Vivek",
            "Branch":"CS",
            "Starting_Year": 2009,
            "Total_Attendance":6,
            "Standing":"A",
            "Year":4,
            "Last_Attendance_Time":"2024-11-23 01:34:32"

        },

        "124":
        {
            "Name": "Nitesh",
            "Branch":"EC",
            "Starting_Year": 2008,
            "Total_Attendance":8,
            "Standing":"AA",
            "Year":3,
            "Last_Attendance_Time":"2024-11-23 01:34:32"

        },

        "125":
        {
            "Name": "Sumit",
            "Branch":"EI",
            "Starting_Year": 2012,
            "Total_Attendance":4,
            "Standing":"B",
            "Year":2,
            "Last_Attendance_Time":"2024-11-23 01:34:32"

        },


    
}

#  To set data in firebase in realtime
for key, value in data.items():
    ref.child(key).set(value)
#...................


#.........Now Add Images(Pics of students) to database(Storage)...

'''Now go to encodeGenerator.py and data(image) to firebase storage because 
everytime you get new data(pics) you need to encode it and update the storage
that's why putting storage code in encodeGenerator.py.

Purpose of this part of code is to compare  '''



