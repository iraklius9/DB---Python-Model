from employee import Employee
from db import conn


employees_data = [
    Employee(name='name1', surname='surname1', age=30),
    Employee(name='name2', surname='surname2', age=25),
    Employee(name='name3', surname='surname3', age=35)
]

for employee in employees_data:
    employee.save()

# employee_id = 1
# employee = Employee.get(employee_id)
# print(employee)

employees = Employee.get_list()
print(employees)

employees = Employee.get_list(surname='surname2', age=25)
print(employees)


conn.commit()
conn.close()
