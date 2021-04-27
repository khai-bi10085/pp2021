courses=[]
coursesID=[]
courses_credit=[]
coursesName=[]

class Course:
    def __init__(self,cid,name,credit):
        self._cid=cid
        self._name=name
        self._credit=credit
        Courses.append(self)
        CoursesID.append(self_.cid)
        Courses_credit.append(self._credit)
        CoursesName.append(self._name)
        
    def get_cid(self):
        return self._cid
    def get_name(self):
        return self._name
    def get_credit(self):
        return self._credit