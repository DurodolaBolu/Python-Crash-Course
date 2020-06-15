import random
secretnumber=random.randint(1,10)
print('enter your name before you proceed: ')
name=input('>>>')
for number_of_guess in range(1,4):
    print('make a guess:')
    guess=int(input('>>>'))
    if guess > secretnumber:
        print('your guess is too high')
    elif guess < secretnumber:
        print('your guess is too low')
    else:
        break
if guess==secretnumber:
    print(f'Bravo! {name}, you got the right number in {number_of_guess} guesses')
else:
    print(f'Oops!, you are wrong!. the right number is actually {secretnumber}')
    