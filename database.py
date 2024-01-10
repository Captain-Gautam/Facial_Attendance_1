import sqlite3


def create_db():
  con = sqlite3.connect('face_recognizer_1.db')
  cursor = con.cursor()

  cursor.execute(''' CREATE TABLE `student` (
    `Student_Id` varchar(30) NOT NULL,
    `Enroll_No` varchar(12) NOT NULL,
    `Student_Name` varchar(30) NOT NULL,
    `Semester` varchar(15) NOT NULL,
    `Dep` varchar(15) NOT NULL,
    `BatchYear` varchar(15) NOT NULL,
    `Year` varchar(15) DEFAULT NULL,
    `Division` varchar(10) DEFAULT NULL,
    `Gender` varchar(15) DEFAULT NULL,
    `DOB` varchar(15) DEFAULT NULL,
    `Email` varchar(30) NOT NULL,
    `Phone_No` varchar(10) NOT NULL,
    `Address` varchar(50) NOT NULL,
    `PhotoSample` varchar(15) DEFAULT NULL,
    PRIMARY KEY (`Student_Id`)
  ) 
      ''' )
  
create_db()
