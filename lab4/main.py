import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

op = curses.initscr() 
curses.start_color()

class Mark:
    def mark_information():
        print("enter the mark :")
        in4m ={
            'cid' : '',
            'sid' : '',
            'value': '' 
        }
        print("enter the course id: ")
        in4m['cid'] = a = input('cid')
        if a in coursesID:
            print("enter the student id: ")
            in4m['sid']=b = input('sid')
            if b in studentsID:
                print("enter the value of mark:")
                in4m['value']=value = float(input('value'))
                if value < 0:
                    print("the mark can not be negative!")
                else:
                    return -1
            else:
                return -1
        else:
            return -1
        mark.append(in4m) 

    def mark_list():
        print("list of the mark: ")
        for i in range(0,len(students)):
            print("course id: ",marks[i]['cid'])
            print("student id: ",marks[i]['sid'])
            print("mark: ",marks[i]['value']) 
