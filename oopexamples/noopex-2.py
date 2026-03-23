class Employee:
    company="SSSIT" # class variable
    def setEmployee(self,eid,ename,esal):
        self.eid  = eid # self.eid is instace variable
        self.ename = ename
        self.esal = esal
    def showEmployee(self):
        print(f'Employee ID     : {self.eid}')
        print(f'Employee Name   : {self.ename}')
        print(f'Employee Salary : {self.esal}')

emp1 =Employee()
emp1.setEmployee(111,"abc",5000)

print("class variable with object : ",emp1.company) # 
print("class variable can be accessed using class name",Employee.company)

print(Employee.eid) # Instance variabele can't be accessed using class name , if we try we get ineprter error




