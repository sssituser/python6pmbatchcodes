class Student:
    def set_Student(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks
    def show_Student(self):
        print(f'Student Id : {self.id}\nStudent Name : {self.name}\nStduetMarks:{self.marks}')
        
s1 = Student()
s1.set_Student(111,"abc",500)
s1.show_Student()

## in the above example self.id,self.name comes under class members.

s2 = Student()
s2.set_Student(112,'kiran',500)
s2.show_Student()