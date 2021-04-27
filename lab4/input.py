import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

op = curses.initscr() 
curses.start_color()

class input:
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
