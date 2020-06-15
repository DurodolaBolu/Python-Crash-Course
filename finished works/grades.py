# program to print the grade of a score between 0.0 and 1.0
score=input('Enter your score: ')
try:
    new_score=float(score)
    if new_score >= 0.0 and new_score <1.0:
        if new_score>=0.9:
            print('A')
        elif new_score >=0.8:
            print('B')
        elif new_score >=0.7:
            print('C')
        elif new_score >=0.6:
            print('D')
        elif new_score < 0.6:
            print('F')
    else:
        print('Bad score!')
except:
    print('Bad score!')