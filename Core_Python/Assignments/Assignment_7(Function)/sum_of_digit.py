# 7. Write a program to find sum of digits of a number.
def sum_digit():

 num=int(input('enter a num='))
 sum=0
 while(num>0):
    dsep=num%10 
    num=num//10 
    sum=sum+dsep
 print(sum) 
sum_digit()    
