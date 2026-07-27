class Employee:
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		
n = int(input('How much employee you want to add ? '))

employees = { }

for i in range(n):
	print(f'\n__-----EMPLOYEE {i+1}-----__')
	name = input('Enter employee Name : ')
	salary = int(input('Eneter employee Salary : '))

	emp = Employee(name,salary)
	
	
	employees[emp.name] = {
	emp.name:emp.salary
	}
	
print('\nEmployee added')
for salary, details in employees.items():
   print(details)
   
employee_name =  input('Enter name to update salary of employee ? ')
employee_salary = int(input('Enter new salary of employee ? '))

if employee_name in employees:

	employees[employee_name] = {
	employee_name:employee_salary
	}
	
	for salary, info in employees.items():
	   print(info)

else:
	print('Employee not found')


employee_search = input('Enter a employee name for search ? ')

if employee_search in employees:
	employees.get(employee_search)
	
	for employee_search in employees.get(employee_search):
		
		print('name:',employee_search,'salary:',employee_salary)

	
else:
	print('Employee not found')