# Question 6: Write a Python program using map() and lambda 
# to check whether each number is even or odd. Return "Even" for
# even numbers and "Odd" for odd numbers.

numbers = [12, 7, 20, 15, 8, 3]
result=list(map(lambda n: 'even' if n%2==0 else 'odd',numbers))
print(result)