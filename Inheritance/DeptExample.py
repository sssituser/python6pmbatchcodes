class Deparatment:
    def __init__(self,did,dname,dloc,dhead):
        self.did = did
        self.dname = dname
        self.dolc = dloc
        self.dhead = dhead
    def showDepartment(self):
        print(f"DeptID : {self.did}")
        print(f"DeptName : {self.dname}")
        print(f'Dept Head : {self.dhead}')
        print(f'Dept location :{self.dolc}')
class Employee(Deparatment):
    def __init__(self,eid,ename,esal,did,dname,dloc,dhead):
        super.__init__(did,dname,dloc,dhead)
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def showEmployee(self):
        print(f"Employee Id :{self.eid}\n Name : {self.ename}\n Salary : {self.esal}")
        
d = Employee(111,"abc",90000,123,"Hr","Raj","Hyd")
d.showEmployee()    
d.showDepartment()
        