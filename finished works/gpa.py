def calc_gpa():
    units=[4,3,2,1]
    print('please, enter the number of courses you are offering below')
    number_of_courses=int(input('>> '))
    count=0
    total_unit=0
    total_quality_point = 0
    while count < number_of_courses:
        print('enter your SCORES and UNITS for each course below')
        score=int(input('your score:'))
        unit=int(input('How many UNIT is the course you entered above: '))
        if score >= 70 and score <= 100 and unit in units:
            point = 5
            total_quality_point += point * unit
            total_unit += unit
        elif score >= 60 and score <= 69 and unit in units:
            point = 4
            total_quality_point += point * unit
            total_unit += unit
        elif score >= 50 and score <= 59 and unit in units:
            point = 3
            total_quality_point += point * unit
            total_unit += unit
        elif score >= 49 and score <= 45 and unit in units:
            point = 2
            total_quality_point += point * unit
            total_unit += unit
        elif score <= 44 and unit in units:
            point = 1
            total_quality_point += point * unit
            total_unit += unit
        count += 1
    gpa= total_quality_point/ total_unit
    rounded_gpa = round(gpa,2)
    return (f' your current GPA is {rounded_gpa}/5.0')


stud_gpa=calc_gpa()
print(stud_gpa)
            
            