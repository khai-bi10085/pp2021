import math
import numpy as np
import curses


students =[]
studentsID =[]
courses =[]
coursesID =[]
marks =[]
marks_detail =[]
gpa_point =[]
course_credit =[]

#op curses

op =curses.initscr()
curses.start_color()

class Student:
    def __init__(self, sid, name, dob):
        self._sid =sid
        self._name =name
        self._dob = dob
        students.append(sefl)
        studentsID.append(self._sid)

    def get_sid(self):
        return self._sid
    def get_name(self):
        return self._name
    def get_dob(self):
        return self._dob 


class Course:
    def __init__(self,cid,name,credit):
        self._cid=cid
        self._name=name
        self._credit=credit
        courses.append(self)
        coursesID.append(self._cid)
        courses_credit.append(self._credit)
        
    def get_cid(self):
        return self._cid
    def get_name(self):
        return self._name
    def get_credit(self):
        return self._credit  

class Mark:
    def __init__(self, cid, sid, value,gpa=0):
        self._sid = sid
        self._cid = cid
        self._value = value
        self._gpa =gpa

    def get_sid(self):
        return self._sid

    def get_cid(self):
        return self._cid

    def get_value(self):
        return self._value
        
    def get_gpa(sefl):
        return sefl._gpa    

#----------------------
class Main:
    #imformation fuction
    def number_of_student():
        while true:
            op.addstr("enter the number of student: ")
            op.refresh()
        count = int(op.getstr().decode())
        if count <= 0:
            print("we don't have any studnents!")
            return 0
        else:
            return count

    def students_information():
       op.addnstr("enter the student id: ", n)
       op.refresh()
       sid =op.getstr().decode()

       op.addnstr("enter the name student: ", n)
       op.refresh()
       name =op.getstr().decode()

       op.addnstr("enter the student dob: ", n)
       op.refresh()
       dob =op.getstr().decode()
       
       Student(sid,name,dob)

    def number_of_course():
        while true:
            op.addstr("enter the number of course: ")
            op.refresh()
        count = int(op.getstr().decode())
        if count <= 0:
            print("we don't have any courses!")
            return 0
        else:
            return count
 

    def course_information():
       op.addnstr("enter the course id: ", n)
       op.refresh()
       cid =op.getstr().decode()

       op.addnstr("enter the name course: ", n)
       op.refresh()
       name =op.getstr().decode()

       op.addnstr("enter the course credit: ", n)
       op.refresh()
       credit = float(op.getstr().decode())
       
       Courses(cid,name,credit)

    def mark_information():
        op.addstr("Enter the course id: ")
        cid = (op.getstr().decode())
        op.clear()
        op.refresh()
        if cid in courseID:
            op.addstr("Enter the student id: ")
            sid=op.getstr().decode()
            op.clear()
            op.refresh()
            if sid in studentID:   
                while True:           
                    op.addstr("Enter the marks: ")
                    value=math.floor(float(op.getstr().decode()))
                    if value<0 or value>10:
                        op.addstr("this mark does not exit!")
                    else:
                        break  
            else:
                exit()
        else:
            exit() 

        Mark(cid,sid,value)
    #------------------------------------

    #list fuction
    def students_list():
        op.addstr("list of student: ")
        op.refresh()
        for a in students:
            op.addstr("student_id: %s    studnent_name:  %s     student_DOB:  %s \n" % (student.get_sid(), student.get_name(), student.get_dob()))
            op.refresh()
    
    def courses_list():
        op.addstr("list of course: ")
        op.refresh()
        for b in courses:
            op.addstr("course_id: %s    course_name:  %s     course_credit:  %s \n" % (course.get_cid(), course.get_name(), course.get_credit()))
            op.refresh()

    def marks_list():
        op.addstr("list of marks: ")
        op.refresh()
        for c in marks:
            op.addstr("course_id_for_mark: %s    student_id_for_mark:  %s     mark:  %s \n" % (mark.get_cid(), mark.get_sid(), mark.get_value()))
            op.refresh()
    #---------------------------

    #gpa fuction
    def gpa():
        value=np.array([mark_detail])
        credit=np.array([course_credit])
        op.addstr("enter student id you want to calculate gpa:")
        sid =op.getstr().decode()
        if sid in studentID:
            for i in range(0,len(students)):
                all_credit=np.sum(credit)
                all_value=np.sum(np.multiply(value,credit))
                op.refresh()
                gpa=all_value/all_credit
                op.refresh()
                    
            else: 
                return 0
            gpa_point.append(gpa)
            op.refresh()
            for c in Mark:
                op.clear()
                op.refresh()
                op.addstr(" Gpa: %s \n" %(gpa()))
                op.refresh()
                break

#----------------------------------
class Display():
    a=Main.number_of_student()
    for i in range(a):
        Main.students_information()
    Main.students_list()
    #----
    b=Main.number_of_course()
    for i in range(b):
        Main.course_information()
    Main.courses_list()
    #----
    Main.mark_information()
    Main.mark_list()

    Main.gpa()

