# a.    1+ 2 + 3 + 4+..... +n

def sum():
    sum=0
    num=int(input('enter a num='))
    for i in range(1,num+1):
     sum=sum+i  
    print(f'sum is : {sum}')    
sum()


# b. 1!+ 2! + 3! + 4!+..... + n!
def factorial_sum(n):
    total = 0
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        total = total + fact
        i = i + 1
    return total
n = int(input("Enter n = "))
print("Sum =", factorial_sum(n))

# c. 1^1 + 2^2 + 3^3+ ...... n^n
def power_sum(n):
    total = 0
    i = 1

    while i <= n:
        total = total + i ** i
        i = i + 1
    return total
n = int(input("Enter n = "))
print("Sum =", power_sum(n))        
  
          

       
    