# function to find the square root of any number
import math
def square_root():
    n = int(input('Enter the number you want to find the square root: '))
    return math.sqrt(n)


print(square_root())

# function to get input from a user and greet them in upper case
def get_input():
    name = input('please enter your name: ')
    return name
def greet_user():
    greet = get_input()
    greeting = f'you are welcome {greet}'
    return greeting.upper()


print(greet_user())

# program to pick two numbers randomely and find the square of the other.
from random import randint
x = randint(1,10)
y = randint (2,5)
print (x**y)

#  program to find factors of a number and their products
class Factor():
    def __init__(self, number):
        self.number = number
    def factors(self):
        facts = []
        for each_num in range(1,self.number+1):
            if self.number%each_num == 0:
                facts.append(each_num)
        return facts
    def factor_multiplier(self):
        multiplier = 1
        for each_num in range(1,self.number+1):
            if self.number%each_num == 0:
                multiplier *= each_num
        return multiplier
    
 
numb = int(input('enter the number you want to find its factor product: '))
Object1 = Factor(numb)
print(Object1.factors())
print(Object1.factor_multiplier())


# A dice rolling simulator having sides 10 and 20 each and roll the dice 10 times
from random import randint
class Dice:
    def __init__(self, sides1 = 10, sides2 = 20):
        self.die1 = sides1
        self.die2 = sides2
    def roll_dice(self):
        counter = 0
        roll_limit = 10
        while counter < 10:
            die1 = randint(1,self.die1)
            die2 = randint(1,self.die2)
            print(f'you rolled {die1} and {die2}')
            counter +=1
            
        
my_dice = Dice()
my_dice.roll_dice()
