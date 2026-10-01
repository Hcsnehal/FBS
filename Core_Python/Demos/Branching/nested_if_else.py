# marks = int(input('tell marks of students :'))
# if (marks>=35):
#     if(marks>=75):
#         print('distinction ')
#     else:
#         if(marks>=60):
#             print('first class')
#         else:
#             print('pass')
# else:
#     print('fail')                    


per = float(input('enter percentage of student :'))
entrance_score = int(input('enter entrance exam score :'))

if(per >= 60):
    if(entrance_score >= 70):
        print('admmission confirm..')
    else:
        print('admission rejected..')
else:
    print('admission rejected...')            
