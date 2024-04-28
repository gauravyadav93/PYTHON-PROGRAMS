class SalaryNotInRangeError(Exception):
    pass
emp_salary = int(input("Enter Employee Salary:-"))
emp_name = input("enter employee name:-")
try:
    if (emp_salary<20000 or emp_salary>50000):
        raise SalaryNotInRangeError
    else:
        print(emp_name)
        print("Salary Is In Range")
except SalaryNotInRange:
    print("SalaryNotInRange is  occuring")
