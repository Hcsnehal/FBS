from functools import reduce 
numbers = [10, 20, 30, 40] 
res=reduce(lambda a,b:a+b,numbers)
print(res)