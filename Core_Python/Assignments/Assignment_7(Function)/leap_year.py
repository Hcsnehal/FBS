def leap_year():
    year=int(input('enter a year..'))
    if(year%400==0 or(year%4==0 and year%10 != 0)):
        print('year is leap year ')
    else:
        print('year is not leap year...')    
leap_year()        