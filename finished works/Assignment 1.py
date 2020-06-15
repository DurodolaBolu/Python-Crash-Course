# Assignment 1:
# Program to reverse a given number and return true if it is the same as the original number
number = int(input('enter any number: '))
original_number = number
Rev = 0
while number>0:
    remainder=number%10
    Rev=Rev*10+remainder
    number=number//10
    if Rev == original_number:
        print("The reversed number is the same as the original")
        break
else:
    print(f'Reverse number is: {Rev}')




