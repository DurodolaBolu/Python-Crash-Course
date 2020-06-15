
         
def grade_point(grade):
    if grade >= 70 and grade <= 100:
        return 5
    elif grade >= 60 and grade <= 69:
        return 4
    elif grade >= 50 and grade <= 59:
        return 3
    elif grade >= 45 and grade <= 49:
        return 2
    elif grade < 44:
        return 1

def gpa():
    total_unit=0
    number_of_courses=0
    course_limit=10
    qp=0
    while number_of_courses < course_limit:
        score=int(input('your score: '))
        if score == '':
            break
        else:
            unit=int(input('enter your unit: '))
            number_of_courses += 1
            total_unit += unit
            quality_point = grade_point(score) * unit
            qp += quality_point
        
    return  quality_point/qp

gpa()

        
        
    
            
            
            
            