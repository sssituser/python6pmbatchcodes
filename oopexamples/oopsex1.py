class Employee:
    EmpId = None    # non static members  , non static member of class we can access using objeet.
    EmpName = None
    EmpSalary = None
    
emp1 = Employee()  # Creation of the object
emp1.EmpId = 111
emp1.EmpName = "Kiran"
emp1.EmpSalary = 50000

print(f'Empoyee ID : {emp1.EmpId}')
print(f'Empoyee Name : {emp1.EmpName}')
print(f'Empoyee Name : {emp1.EmpSalary}')

# Empoyee  to object

emp2 = Employee()  # Creation of the object
emp2.EmpId = 112
emp2.EmpName = "Raj"
emp1.EmpSalary = 50000

print(f'Empoyee ID : {emp2.EmpId}')
print(f'Empoyee Name : {emp2.EmpName}')
print(f'Empoyee Name : {emp2.EmpSalary}')