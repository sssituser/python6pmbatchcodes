class Student:
    def setsudent(self,sid,sname,smarks):
        self.sid = sid
        self.sname = sname
        self.smarks =smarks
        return
    def getstudent(self):
        print(f'Student ID : {self.sid}')
        print(f'Student Name : {self.sname}')
        print(f'Student Marks : {self.smarks}')
        return
        
s1 = Student()
s1.setsudent(111,"krian",500)
s1.getstudent()

s2 = Student()
s2.setsudent(112,"Raj",500)
s2.getstudent()