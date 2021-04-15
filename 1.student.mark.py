students =[]
studentsID =[]
courses =[]
coursesID =[]
marks =[]

def number_of_student():
    count = int(input("enter the number of student: "))
    if count <=0:
        print("we don't have any studnents!")
        return 0
    else:
        return count 

def students_information():
    print("enter the students' information: ")
    in4 = {
        'sid': '',
        'name': '',
        'DOB': ''
    }

    print("enter the id student: ")
    in4['sid'] =sid= input('sid:')
    print("enter the student name: ")
    in4['name']=input()
    print ("enter the DOB of student: ")
    in4['DOB']= input()
    students.append(in4)
    studentsID.append(sid)



def students_list():
    print("list of students: ")
    for i in range(0,len(students)):
        print("[",students[i]['sid'],"]")
        print("[",students[i]['name'],"]")
        print("[",students[i]['DOB'],"]")
#------------------------------------------

def number_of_course():
    count = int(input("enter the number of course: "))
    if count <=0:
        print("we don't have any courses!")
        return 0
    else:
        return count 

def course_information():
    print("enter the courses' information: ")
    in4c = {
        'cid': '',
        'name':' '
    }
    print("enter the id course: ")
    in4c['cid'] =cid = input('cid:')
    print("enter the course name: ")
    in4c['name']= input()
    courses.append(in4c)
    coursesID.append(cid)

def courses_list():
    print("list of the courses: ") 
    for i in range(0,len(courses)):
        print("[",courses[i]['cid'],"] ")
        print("[",courses[i]['name'],"]")   
#------------------------------------

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
        print("[",marks[i]['cid'],"]")
        print("[",marks[i]['sid'],"]")
        print("[",marks[i]['value'],"]") 


#display
a=number_of_student()
for i in range(a):
     students_information()
students_list()
#----
b=number_of_course()
for i in range(b):
    course_information()
courses_list()
#----
mark_information()
mark_list()



