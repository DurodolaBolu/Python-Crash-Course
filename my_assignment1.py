''' this program acquire details of staffs in a company of 30 workers,
and from their monthly salary deduce if they are middle class citizen or not,
'''
# initial definition of a function to calculate the yearly salary
def yearly_salary(salary):
    return salary * 12

# current registered employees data base
Employees={'staff00':['Ayodele', 'Benson', 'male', 45, 1800],
           'staff01':['Boluwatife', 'Durodola','male', 23, 2500],
           'staff02':['Akin', 'Ayodeji', 'male', 25, 600],
           'staff03':['kayode','Olabode','male',37, 800],
           'staff04':['Elizabeth', 'Akinsiku', 'female', 19, 740],
           'staff05':['Boluwatife', 'Odufuwa', 'female', 27, 800],
           'staff06':['Abayomi', 'Olawumi', 'male', 39, 1500]
           }

totalnumber=30
count=0
while count <= totalnumber:
    print('your id must be preceded by "staff" and your entry number. e.g "staff00"')
    print('please, enter your staff id below to check: ')
    staff_id=input('\n>>')
    if staff_id in Employees:
        first_name=Employees[staff_id][0]
        last_name=Employees[staff_id][1]
        yearlySalary=yearly_salary(Employees[staff_id][4])
        if yearlySalary > 10000:
            print(f'{first_name} {last_name} is greater than a middle class citizen') 
        else:
            print(f'{first_name} {last_name} is a middle class citizen')
        count+=1
        break
        
    else:
        print('sorry, your details are not in the database.Add your details below')
        firstName=input('enter your first name: ')
        lastName=input('enter your last name: ')
        sex=input('your sex please: ')
        age=input('what is your current age: ')
        salary=int(input('How much do you earn per month:$ '))
        details=[firstName,lastName,sex,age,salary]
        Employees[staff_id]=details
        print('Enter your staff id again to check')
        
