def number_of_student():
    count = int(input("enter the number of student: "))
    if count <=0:
        print("we don't have any studnents!")
        return 0
    else:
        return count       
            
def student_information():
    print("enter the information of students: ")
    id_student = input("id of students: ")
    name_student = input(("name of students: "))
    DOB_student = input(("DOB of students: "))
    a = {"id of studnets:": id_student, "name of student": name_student, "DOB of student": DOB_student}
    return a

def list_student(Studentlist):
    for a in Studentlist:
        print(f"id_student is {a['id of student']},name_student is {a['name of student']}, DOB_student is {a['DOB of student']}")

def number_of_course():
    count = int(input("enter the number of course: "))
    if count <=0:
        print("we don't have any courses!")
        return 0
    else:
        return count 
    
def course_information():
    print("enter the information of courses: ")
    id_course = input("id of courses: ")
    name_course = input(("name of courses: "))
    b = {"id of course:": id_course, "name of course": name_course}
    return b

def list_course(Courselist):
    for b in Courselist:
        print(f"id_course is {b['id of course']},name_course is {b['name of course']}")


Studentlist =[]
count = number_of_student()
for i in range (0, count):
    a = student_information()
    Studentlist += [a]

Courselist =[]
count = number_of_course()()
for i in range (0, count):
    b = student_course()
    Courselist += [b]
    

print("all students: ")
list_student(Studentlist)
print("all courses: ")
list_course(Courselist)

name_student =str(input("Enter student name: "))
id_student =str(input("Enter student id: "))
DOB_student =str(input("Enter student DOB: "))
mark =str(input("Enter python mark: "))

print("list of student's mark: ")
print("Student name : ",name_student )
print("Student id : ",id_student)
print("Student DOB : ",DOB_student )
print("Student mark : ",mark )
