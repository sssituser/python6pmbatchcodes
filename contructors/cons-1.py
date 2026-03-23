class Employee:
    
    def __init__(self,eid,ename,esal):
        print('Hi Iam constuructor with parameters')
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getmployoee(self):
        print(f'Employee ID :{self.eid}')
        print(f'Employee Name : {self.ename}')
        print(f'Employee salary : {self.esal}')
    
emp1 = Employee(111,"Ravi",60000)
emp1.getmployoee()