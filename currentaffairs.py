from QuestionBank import question_banks
import json
class CurrentAffairs:
    def __init__(self, prompt, answer):
        self.prompt=prompt
        self.answer=answer


questions=[CurrentAffairs(question_banks[0],'a'),
           CurrentAffairs(question_banks[1],'a'),
           CurrentAffairs(question_banks[2],'b'),
           CurrentAffairs(question_banks[3],'c'),
           CurrentAffairs(question_banks[4],'b'),
           CurrentAffairs(question_banks[5],'b')
          ]


User_id={'user1':'Durodola Boluwatife',
       'user2':'Olabode Kayode',
       'user3':'Akinsiku Elizabeth',
       'user4' : 'Odufuwa Boluwatife',
        'user5': 'Olawumi Abayomi'
        
       }



def run_test(questions):
    score=0
    while True:
        username = input('enter your user id\n>> ')
        if username in User_id:
            for question in questions:
                answer=input(question.prompt)
                if answer.lower()==question.answer:
                    score+=1
            print(f'{User_id[username]}, You got {score}/{len(questions)} questions correctly')
        else:
            print('you are not registered!, Get yourself registered below: ')
            name = input('enter your name: ')
            User_id.update({username:name})
            print('Congratulations, you have succesfully been registered. Refresh to continue\n')
        
    

run_test(questions)



    
