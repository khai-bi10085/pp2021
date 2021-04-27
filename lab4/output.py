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