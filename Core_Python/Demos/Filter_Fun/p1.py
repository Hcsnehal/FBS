# Question: Write a Python program using filter() 
# and lambda to select all the 
# negative numbers from a list.

numbers = [10, -5, 20, -15, 0, -8, 12]
res=list(filter(lambda n:n < 0,numbers))
print(res)