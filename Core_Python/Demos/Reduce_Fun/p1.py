# Write a Python program using reduce() and lambda to
# multiply all the numbers in a list.
from functools import reduce
numbers = [2, 3, 4, 5]
res=reduce(lambda a,b:a*b,numbers)
print(res)