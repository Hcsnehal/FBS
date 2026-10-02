#1. WAP to print all even numbers until n.  

# n=int(input('enter n='))

# i=1
# while(i<=n):
#     if(i%2==0):
#         print(i)
#     i+=1 

# 3. WAP to print sum of series upto n.

# n=int(input('enter a n='))
# sum=0
# i=0
# while(i<=n):
#     sum=sum+i  
#     i+=1 
# print(sum)  
#   

# 4. WAP to print factorial of a number .

# num=int(input('enter a num='))
# fact=1
# i=1
# while(i<=num):
#     fact=fact*i 
#     i+=1 
# print(fact)    

# 5. WAP to print Fibonacci series upto n.
# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# i = 1
# while i <= n:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     i += 1


# 6. WAP to check if a given number is prime number or not.

# num=int(input('enter a num='))
# if(num<=1):
#     print('num is not prime number=')
# else:
#     i=1
#     cout=0
#     while(i<=num):
#         if(num%i==0):
#             cout+=1 
#         i+=1

#     if(cout==2):
#             print('num is prime')
#     else:
#             print('num is not prime.')       


# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.   
# num=int(input('enter a num='))
# i=0
# while(i<=num):
#     if(i%2!=0 and  i%3!=0):
#         print(i)  
#     i+=1    
     
    
# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

# start=int(input('enter a start num='))
# end=int(input('enter a end num'))

# i=0
# while(i<=end):
#     if(i%7==0 and i%5==0):
#         print(i)  
#     i+=1    

# 9. WAP to print all numbers in a range divisible by a given number.
start=int(input('enter a start num='))
end=int(input('enter a end num='))
given_num=int(input('enter a given num='))
i=1
if(given_num != i):
    print('num is not in a range..')

while(i<=end):
    if(given_num % i==0):
        print(i)
    i+=1    

    
 


