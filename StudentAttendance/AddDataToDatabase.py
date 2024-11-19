import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://studattendance-379b1-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data ={
    "100603":
        {
            "name": "Ashish A Ankam",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 9,
            "gpa": 8.7,
            "sem": 6,
            "last_attendance_time": "2024-06-12 10:01:44"
        },
    "130603":
        {
            "name": "Yashas M B",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 4,
            "gpa": 7.7,
            "sem": 6,
            "last_attendance_time": "2024-06-07 12:03:34"
        },
        "291103":
                {
                    "name":  "Srujan V",
                    "branch": "AIML",
                    "starting_year": 2021,
                    "total_attendance": 11,
                    "gpa": 9.7,
                    "sem": 6,
                    "last_attendance_time": "2024-6-11 03:54:34"
        },
                "021003":
                {
                    "name":  "Anusha S",
                    "branch": "CSE",
                    "starting_year": 2021,
                    "total_attendance": 10,
                    "gpa": 9.2,
                    "sem": 6,
                    "last_attendance_time": "2024-6-4 03:54:34"
        }



}

for key,value in data.items():
    ref.child(key).set(value)