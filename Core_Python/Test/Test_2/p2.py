# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.


digit= int(input('enter a three digit num :'))
d1=digit % 10  # 3
d1_sep=digit//10 #12

d2=d1_sep % 10  #2

d3=d1_sep // 10 #1

con1 = d3 == 2 * d2
con2 = d3 == 1/2 * d1

if con1 and con2:
    print("yes,you have done it ")
else:
    print("plz try next time")    

