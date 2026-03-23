class Employee:
    deparatementName:str = "Developmenet" # class variable  or static variable
    def setemployee(self,eid,ename,esal):
        self.eid = eid  # self.eid is instance variable , and eid local variable
        self.ename = ename
        self.esal = esal
    def getemployee(self):
        print(f'EmployeeID :{self.eid}')
        print(f'Employee Name : {self.ename}')
        print(f'Employee salary : {self.esal}')
        print(f'Department : {self.deparatementName}')
emp1 = Employee() # reation of object

emp1.setemployee(111,"vamsi",45000)
emp1.getemployee()

emp2 = Employee()
emp2.setemployee(112,"Sudheer",50000)
emp2.getemployee()

emp3 = Employee()
emp3.setemployee(112,"Hrushikesh",55000)
emp3.getemployee()

