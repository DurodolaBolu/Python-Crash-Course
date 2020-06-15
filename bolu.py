number =  eval(input('how tall do you want it to be: '))
for i in range(1, number, 2):
    print('*' * i )
for i in range(number,-2):
    print('*' * i)
