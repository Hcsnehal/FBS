#Write a program to swap two numbers using third variable. num1 = 10 , num2 = 20
num1=int(input('enter num1 :'))
num2 = int(input('enter num2 :'))

print(f'before swapping num 1 is {num1} and num2 is {num2}')

temp=num1  # 10
num1= num2 # 20
num2 = temp #10

print(f'after swapping num1 is {num1} and num2 is {num2}')  