# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 = int(input('enter marks of first subject:'))
sub2 = int(input('enter marks of 2nd subject:'))
sub3 = int(input('enter marks of third subject:'))
sub4 = int(input('enter marks of 4th subject:'))
sub5 = int(input('enter marks of 5th subject:'))

total_marks = sub1+sub2+sub3+sub4+sub5
per_centage = (total_marks/500)*100

if per_centage >= 90:
    print('first class with distinction..')
elif per_centage >= 75:
    print('second class...')
elif per_centage >= 60:
    print('third class....')
elif per_centage >= 35:
    print('pass..') 
elif per_centage < 35:
    print('fail...')
else:
    print('enter valid marks....')          


