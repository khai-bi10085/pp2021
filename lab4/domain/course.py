courses=[]
coursesID=[]
courses_credit=[]
coursesName=[]

class Course:
    def __init__(self,cid,name,credit):
        self._cid=cid
        self._name=name
        self._credit=credit
        courses.append(self)
        coursesID.append(self_.cid)
        courses_credit.append(self._credit)
        coursesName.append(self._name)
        
    def get_cid(self):
        return self._cid
    def get_name(self):
        return self._name
    def get_credit(self):
        return self._credit