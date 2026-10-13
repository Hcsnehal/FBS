# 1. Write a program to accept year from user and check if it is a leap year or not.
year = int(input("Enter a year: "))
if year % 400 == 0:
    print('year is leap year..')
elif year % 100 == 0:
    print('year is not leap year.')
elif year % 4 == 0:
    print('year is leap year..')
else:
    print('year is not leap year')