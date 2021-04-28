import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

op = curses.initscr() 
curses.start_color()
class Main:
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