import math
import numpy as np
import curses


students =[]
studentsID =[]
courses =[]
coursesID =[]
marks =[]
marks_detail =[]
marks_gpa =[]
course_credit =[]

#screen curses
screen =curses.initscr()
curses.start_color()
#-------------

class Student:
    def __init__(self, sid, name, dob):
        self._sid =sid
        self._name =name
        self._dob = dob
        students.append(sefl)
        studentsID.append(self._sid)

    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_dob(self):
        return self._dob 




    def number_of_student():
        while true:
            screen.addstr("enter the number of student: ")
            screen.refresh()
        count = int(screen.getstr().decode())
        if count <= 0:
            print("we don't have any studnents!")
            return 0
        else:
            return count

    def students_information():
       screen.addnstr("enter the student id: ", n)
       screen.refresh()
       sid =screen.getstr().decode()

       screen.addnstr("enter the name student: ", n)
       screen.refresh()
       name =screen.getstr().decode()

       screen.addnstr("enter the student dob: ", n)
       screen.refresh()
       dob =screen.getstr().decode()
       
       students(sid,name,dob)



    def students_list():
        print("list of students: ")
        for i in range(0, len(students)):
            print("id student: ", students[i]['sid'])
            print("student name: ", students[i]['name'])
            print("student DOB", students[i]['DOB'])
#------------------------------------------
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




    def number_of_course():
        while true:
            screen.addstr("enter the number of course: ")
            screen.refresh()
        count = int(screen.getstr().decode())
        if count <= 0:
            print("we don't have any courses!")
            return 0
        else:
            return count
 

    def course_information():
       screen.addnstr("enter the course id: ", n)
       screen.refresh()
       cid =screen.getstr().decode()

       screen.addnstr("enter the name course: ", n)
       screen.refresh()
       name =screen.getstr().decode()

       screen.addnstr("enter the course credit: ", n)
       screen.refresh()
       credit = float(screen.getstr().decode())
       
       courses(cid,name,credit)

    def courses_list():
        print("list of the courses: ") 
        for i in range(0,len(courses)):
            print("id course: ",courses[i]['cid'])
            print("name course: ",courses[i]['name'],)   
#------------------------------------
class Mark:
    def __init__(self, cid, sid, value,gpa=0):
        self._sid = sid
        self._cid = cid
        self._value = value
        self._gpa =gpa
        engine.marks.append(self)

    def get_sid(self):
        return self._sid

    def get_cid(self):
        return self._cid

    def get_value(self):
        return self._value
        
    def get_gpa(sefl):
        return sefl._gpa    


    def mark_information():
        screen.addstr("Enter the course id: ")
    cid = (screen.getstr().decode())
    screen.clear()
    screen.refresh()
    if cid in courseID:
        screen.addstr("Enter the student id: ")
        sid=screen.getstr().decode()
        screen.clear()
        screen.refresh()
        if sid in studentID:   
            while True:           
                screen.addstr("Enter the marks: ")
                value=math.floor(float(screen.getstr().decode()))
                if value<0 or value>10:
                    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                    try:
                        screen.addstr("the value is not valid!", curses.color_pair(1))
                    except curses.error:
                            pass
                    screen.refresh()
                    curses.napms(1000)
                    screen.clear()
                    screen.refresh()
                    screen.addstr("Please enter any number you want: \n")
                    value=math.floor(float(screen.getstr().decode()))
                else:
                    break  
        else:
            exit()
    else:
        exit() 

    marks(cid,sid,value)

    def gpa():
        marks=np.array([mark_detail])
        points=np.array([course_credit])
        screen.addstr("Enter student id that you want to get gpa:")
        sid =screen.getstr().decode()
        if sid in studentID:
            for i in range(len(students)):
                totalCredit=np.sum(points)
                totalValue=np.sum(np.multiply(marks,points))
                screen.refresh()
                gpa = totalValue/totalCredit
                screen.refresh() 
        else: 
                return 0
    
        Mark_gpa.append(gpa)
        py.refresh()
        for value in marks:
                 py.clear()
                 py.refresh()
                 py.addstr(" [Mark_studentid: ] %s   [Gpa: ]%s \n" %(mark.get_id(),gpa))
                 py.refresh()
               
                 break             



#display
class Display:
    a=Student.number_of_student()
    for i in range(a):
        Student.students_information()
    Student.students_list()
    #----
    b=Course.number_of_course()
    for i in range(b):
        Course.course_information()
    Course.courses_list()
    #----
    Mark.mark_information()
    Mark.mark_list()



