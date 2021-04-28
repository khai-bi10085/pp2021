import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

op = curses.initscr() 
curses.start_color()

class output:
    def students_list():
        op.addstr("list of student: ")
        op.refresh()
        for a in students:
            op.addstr("student_id: %s    studnent_name:  %s     student_DOB:  %s \n" % (a.get_sid(), a.get_name(), a.get_dob()))
            op.refresh()
    
    def courses_list():
        op.addstr("list of course: ")
        op.refresh()
        for b in courses:
            op.addstr("course_id: %s    course_name:  %s     course_credit:  %s \n" % (b.get_cid(), b.get_name(), b.get_credit()))
            op.refresh()

    def marks_list():
        op.addstr("list of marks: ")
        op.refresh()
        for c in marks:
            op.addstr("course_id_for_mark: %s    student_id_for_mark:  %s     mark:  %s \n" % (c.get_cid(), c.get_sid(), c.get_value()))
            op.refresh()