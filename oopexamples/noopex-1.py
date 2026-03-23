class Employee:
    empId = 111
    empName = "abc"
    empSal = 50000
    def showEmployee():
        print(f'Employee ID      = {Employee.empId}')
        print(f'Employee Name    = {Employee.empName}')
        print(f'Employee Salary  = {Employee.empSal}')

print(f'Employee ID      : {Employee.empId}')
print(f'Employee Name    : {Employee.empName}')
print(f'Employee Salary  : {Employee.empSal}')
Employee.showEmployee()
