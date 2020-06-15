#program to print each element of a string from the back

enter_a_string=input('enter a string: ')
length=len(enter_a_string)
index=len(enter_a_string)-1
while index<length:
    print(enter_a_string[index])
    index-=1
    if index==-1:break
        
