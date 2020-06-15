print('This is a number guessing game and it requires you to input your name.')
print('Note: the correct number is between 1 - 9')
name = input(('kindly enter your name:'))
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("make a guess:"))
    guess_count += 1
    if guess == secret_number:
        print(f'Bravo! {name}, you won!')
        break
else:
    print(f'Oops! {name}, you failed')
