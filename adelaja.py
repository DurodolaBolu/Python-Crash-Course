'''This a class for exam and record unit to
   print out the name, matric number and semester GPA of
   certain number of students in a dept
'''
class student:
   def __init__(self,studentname,matricno,age):
        self.name=studentname
        self.matricno=matricno
        self.age=age
    
   def studgpa(self):

        totalunits=0
        cumpoint=0
        units= [4,3,2,1]
        course_count = 0
        course_no = int(input('\nHow many courses are you offering this semester:\n>>'))
        print('\nENTER EACH COURSE SCORE AND UNIT ONE AFTER THE OTHER')
        while course_count < course_no:
            score = int(input('\nWhat is the score for this particular course:\n>> '))
            unit = int(input('what is the unit of the course you entered above:\n> '))
            if score>=70 and score<=100 and unit in units:
                point=5
                cumpoint+=point*unit
                totalunits += unit
            elif score>=60 and score<=69 and unit in units:
                point=4
                cumpoint +=point*unit
                totalunits += unit
            elif score>=50 and score<=59 and unit in units:
                point=3
                cumpoint+=point*unit
                totalunits += unit
            elif score>=45 and score<=49 and unit in units:
                point=2
                cumpoint += point*unit
                totalunits += unit
            elif score < 44 and unit in units:
                point=1
                cumpoint+= point*unit
                totalunits += unit
            course_count += 1
        gpa= round(cumpoint/totalunits, 2)
        return gpa


number_of_students = int(input('Enter the total number of students in this department\n>>> '))
student_count = 0
while student_count < number_of_students:
    firstname = input("Enter student's first name: ")
    lastname = input("Enter student' last name: ")
    matric = input("Enter student's matric number: ")
    name = f'{firstname} {lastname}'
    age = int(input('Enter students age: '))
    student1 = student(name, matric, age)
    print(f'The gpa of {student1.name} with matric number {student1.matricno} is {student1.studgpa()}/5.0\n')
    student_count += 1



