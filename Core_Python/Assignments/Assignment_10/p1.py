# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

li = [67,43,12,34,21,22,90]
Even_List = []
Odd_List = []

for val in li:
    if val % 2 == 0:
        Even_List.append(val)
    else:
        Odd_List.append(val)
print('Even elements list=',Even_List)
print('Odd Elements List=',Odd_List)