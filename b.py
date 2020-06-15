from random import  choice
def roll_dice1():
    dice1 = range(1,7)
    return choice(dice1)
def roll_dice2():
    dice2 = range(1,7)
    return choice(dice2)
def roll_dice():
    while True:
        print('Do you want to roll dice now? Type Y to continue, N to exit')
        instruct = input('>> ').lower()
        if instruct == 'y':
            print(f'You rolled {roll_dice1()} and {roll_dice2()}\n\n')
        elif instruct == 'n':
            break
        else:
            print('sorry, i dont understand this command, type either Y or N\n\n')
                
            
roll_dice()


    
