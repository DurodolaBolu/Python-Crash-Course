#Assignment 2
# program to create a list of numbers containing both even and odd numbers from two list of numbers defined
# set the the two list of numbers
# i set the new list we are trying to create to be empty
new_list = []
#  create two list of numbers
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# i then check for odd and even numbers in the lists then insert it into the empty new_list
for each_num in list1:
    if each_num%2 ==0:
        new_list.append(each_num)
for each_num in list2:
    if each_num%2==1:
        new_list.append(each_num)
print(f'The new list is: {new_list}')
