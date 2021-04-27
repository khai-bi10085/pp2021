marks=[]
mark_detail=[]
gpa_point=[]


class Mark:
    def __init__(self, cid, sid, value,gpa=0):
        self._sid = sid
        self._cid = cid
        self._value = value
        self._gpa =gpa
        mark.append(self)
        mark_detail.append(self._value)


    def get_sid(self):
        return self._sid

    def get_cid(self):
        return self._cid

    def get_value(self):
        return self._value
        
    def get_gpa(sefl):
        return sefl._gpa    

