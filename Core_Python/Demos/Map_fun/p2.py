# Question: Write a Python program using map() and lambda to 
# convert each number in the
# list into its square, then add 5 to the result.

numbers = [2, 4, 6, 8, 10]
res=list(map(lambda n:(n*n)+5 ,numbers))
print(res)