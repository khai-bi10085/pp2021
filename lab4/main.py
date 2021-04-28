import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

op = curses.initscr() 
curses.start_color()
class Main:
    a=input.number_of_student()
    for i in range(a):
        input.students_information()
    output.students_list()
    #----
    b=input.number_of_course()
    for i in range(b):
        input.course_information()
    output.courses_list()
    #----
    input.mark_information()
    output.mark_list()

    input.gpa()