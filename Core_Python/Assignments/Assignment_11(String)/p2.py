# Python Program to Remove the nth Index Character from a Non-Empty
# String

str='snehalDeshmukh'
n=int(input('enter index of string to remove character='))
new_s=str[:n]+str[n+1:]
print(new_s)