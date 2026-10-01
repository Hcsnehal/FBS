# 10. Write a program to reverse three-digit number.
num=234

rem1=num%10 #4
num1=num//10 #23

rem2 = num1%10 #3
num2 = num1//10 #2

rev = rem1*100+rem2*10+num2

print(f'reverse of {num} is {rev}')