# 6. WAP to check if a given number is prime number or not.

num = int(input('enter a num='))

if num <= 1:
    print('num is not a prime number')
else:
    i=1
    count=0
    while(i<=num):
     if(num%i==0):
        count+=1
     i+=1

    if count == 2:
       print('num is prime ')
    else:
       print('num is not prime.')   

