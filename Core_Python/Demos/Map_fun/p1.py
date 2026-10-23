# Write a Python program using map() and lambda 
# to add 10 to every element in a list.

numbers = [5, 12, 20, 7, 15]
res=list(map(lambda n:n+10,numbers))
print(res)