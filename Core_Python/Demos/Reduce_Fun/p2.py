# Write a Python program using reduce() and lambda to
# find the largest number in a list.
from functools import reduce
numbers = [12, 45, 23, 67, 34, 89, 56]
res=reduce(lambda a,b: a if a>b else b,numbers)
print(res)