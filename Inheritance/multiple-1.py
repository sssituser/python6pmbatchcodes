class School:
    def ssccbse(self,per):
        self.per =per
        print(f"I Have completed x with percentage  {self.per}")
class Inter:
    def inter(self,per):
        print(f"I have completed Inter with Percentage {self.per}")
class Graduation:
    def bahelor(self,grade):
        self.garde = grade
        print(f"I have completed bachelors with Garde of {self.garde}")
    
class Student(School,Inter,Graduation):
    def getStudent(self,name):
        self.name = name
        print(f"Hi Iam  {self.name}")
s1 = Student()
s1.getStudent("Kiran")
s1.ssccbse(78)
s1.inter(90)
s1.bahelor(8.9)
