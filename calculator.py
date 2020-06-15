def calculator():
    num1 = float(input('Enter your first number: '))
    op = input('what operation do you want to perfrom:  ')
    num2 = float(input('Enter your second number: '))
    if op == '+' or op.lower() == 'addition' or op.lower() == 'plus':
        return num1 + num2
    elif op == '-' or op.lower() == 'subtraction' or op.lower() == 'minus':
        return num1 - num2
    elif op == '*' or op.lower() == 'multiplication' or op.lower() == 'multiply':
        return num1 * num2
    elif op == '/' or op.lower() == 'division' or op.lower() == 'divide':
        return num1 / num2
    else:
        return 'enter a valid operator'
    
print(calculator())
    
    