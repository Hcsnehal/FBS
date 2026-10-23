# Question 5: Write a Python program using map() and lambda to 
# convert each negative number into a positive number by multiplying 
# it by -1. Leave positive numbers unchanged.

numbers = [-5, 10, -15, 20, -25]
res=list(map(lambda n:n*(-1) if n<0 else n ,numbers))
print(res)