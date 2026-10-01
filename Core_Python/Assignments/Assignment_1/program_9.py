# Write a program to swap two numbers without using third variable.
a = int(input('enter a num1:'))
b = int(input('enter a num2:'))

a = a+b
b = a-b
a = a- b

print(f'after swapping value of a is {a} and b is {b}')