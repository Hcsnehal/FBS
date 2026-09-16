# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gender = input('enter gender of person(m/f)=')
age = int(input('enter age='))

if age > 0 and age<100 :
    if gender == 'm':
        if age >= 21:
            print('this male is eligible for marrage..')
        else:
            print('this male is not eligible for marrage..')
    elif gender == 'f':
        if age >= 18 :
            print('this lady is eligible for marrage..')
        else:
            print('this lady is not eligible for marrage...')
    else:
        print('enter valid gender..')
else:
    print('enter valid age number..')                        
