# Find the sum of three-digit number. 123
num=int(input('enter a num :'))

r1 = num%10 #3
num1= num // 10  #12

r2 = num1 % 10 #2
num2 = num1 // 10 #1

r3 = num2

sum = r1+r2+r3
print(f'sum is {sum}')
