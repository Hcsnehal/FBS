# WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

#da= Dearness Allowance
#ta=travel allovance
#hra = House Rent Allowance

Basic_sal = float(input('enter a basic salary :'))

da = (Basic_sal*10)/100
ta = (Basic_sal*12)/100
hra = (Basic_sal*15)/100

total_salary = Basic_sal + da + ta + hra
print(f'da is {da}')
print(f'ta is {ta}')
print(f'hra is {hra}')

print(f'total salary is {total_salary}')

