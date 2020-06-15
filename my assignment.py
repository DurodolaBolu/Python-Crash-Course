""" program to get the personal details of a few employees of a company,
their monthly salary in USD($) and check if theY are middle class citizen or not
"""
def yearly_salary(salary):
    return salary*12
        
number_of_employees=0
name_of_employees=[]
salary_of_employees=[]
while number_of_employees < 6:
    name=input('enter your full name: ')
    your_salary=int(input(('enter your monthly salary:$')))
    name_of_employees.append(name)
    salary_of_employees.append(your_salary)
    number_of_employees +=1
print(f'this is the full name of the employees {name_of_employees}')\
 
# name of employees and their monthly salary in USD($)
name_of_employees_and_salary=dict(zip(name_of_employees,salary_of_employees))
print(f'This is the name of employees with their monthly salary{name_of_employees_and_salary}')\

''' Salary of employees per year and checking if they are
middle class citizen
'''
salary_in_list=salary_of_employees
if yearly_salary(salary_in_list[0]) > 10000:
    print(f'{name_of_employees[0]} is not a middle class citizen')
else:
    print(f'{name_of_employees[0]} is a middle class citizen')

if yearly_salary(salary_in_list[1]) > 10000:
    print(f'{name_of_employees[1]} is not a middle class citizen')
else:
    print(f'{name_of_employees[1]} is a middle class citizen')

if yearly_salary(salary_in_list[2]) > 10000:
    print(f'{name_of_employees[2]} is not a middle class citizen')
else:
    print(f'{name_of_employees[2]} is a middle class citizen')
    
if yearly_salary(salary_in_list[3]) > 10000:
    print(f'{name_of_employees[3]} is not a middle class citizen')
else:
    print(f'{name_of_employees[3]} is a middle class citizen')
    
if yearly_salary(salary_in_list[4]) > 10000:
    print(f'{name_of_employees[4]} is not a middle class citizen')
else:
    print(f'{name_of_employees[4]} is a middle class citizen')

if yearly_salary(salary_in_list[5]) > 10000:
    print(f'{name_of_employees[5]} is not a middle class citizen')
else:
    print(f'{name_of_employees[5]} is a middle class citizen')

    