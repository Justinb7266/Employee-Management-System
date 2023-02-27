# this is the project to enter employee information
# input for employee name
employeeName = str(input('Employee Name: '))
# input for employee SSN
employeeSSN = str(input('Employee SSN: '))
# input for employee Phone
employeePhone = str(input('Employee Phone Number: '))
# input for employee email
employeeEmail = str(input('Employee Email: '))
# input for employee salary
employeeSalary = int(input('Employee Salary: '))

# dispaly output as required
print("--------------------",employeeName,"--------------------")
print("SSN:",employeeSSN)
print("Phone:",employeePhone)
print("Email:",employeeEmail)
print("Salary: $",employeeSalary,sep="")
print("_________________________________________________________")