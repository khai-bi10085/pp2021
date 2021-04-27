students=[]
studentID=[]
student_Name=[]
studentdob=[]
class  Ssudent:
    def __init__(self,sid,name,dob):
        self._sid=sid
        self._name=name
        self._dob=dob
        students.append(self) 
        studentID.append(self._sid)
        studentName.append(self._name)
        Studentdob.append(self._dob)
        
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_dob(self):
        return self._dob