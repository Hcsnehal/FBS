# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age_1 = int(input('enter the age of first person='))
ticket1 = int(input('enter ticket amt='))

age_2 = int(input('enter the age of second person='))
ticket2 = int(input('enter ticket amt='))

age_3 = int(input('enter the age of third person='))
ticket3 = int(input('enter ticket amt='))

age_4 = int(input('enter the age of forth person='))
ticket4= int(input('enter ticket amt='))

age_5 = int(input('enter the age of fifth person='))
ticket5= int(input('enter ticket amt='))

total_amt = 0
#person 1 :
if age_1 < 12:
    disco = ticket1 * 30/100 
    tic_amt = ticket1 - disco
    print(f'children : discount={disco} ticketamout={tic_amt}')
elif age_1 > 59:
    disco = ticket1 * 50/100
    tic_amt = ticket1 - disco
    print(f'adult: discount={disco} ticketamount={tic_amt}')   
else:
    tic_amt = ticket1
    total_amt = total_amt+tic_amt

    
#p2
if age_2 < 12:
    disco = ticket2 * 30/100 
    tic_amt = ticket2 - disco
    print(f'children : discount={disco} ticketamout={tic_amt}')
elif age_2 > 59:
    disco = ticket2 * 50/100
    tic_amt = ticket2 - disco
    print(f'adult: discount={disco} ticketamount={tic_amt}')   
else:
    tic_amt = ticket2
    total_amt = total_amt+tic_amt

#p3
if age_3< 12:
    disco = ticket3 * 30/100 
    tic_amt = ticket3 - disco
    print(f'children : discount={disco} ticketamout={tic_amt}')
elif age_3 > 59:
    disco = ticket3 * 50/100
    tic_amt = ticket3 - disco
    print(f'adult: discount={disco} ticketamount={tic_amt}')   
else:
    tic_amt = ticket3
    total_amt = total_amt+tic_amt

#p4
if age_4 < 12:
    disco = ticket4 * 30/100 
    tic_amt = ticket4 - disco
    print(f'children : discount={disco} ticketamout={tic_amt}')
elif age_4> 59:
    disco = ticket4 * 50/100
    tic_amt = ticket4 - disco
    print(f'adult: discount={disco} ticketamount={tic_amt}')   
else:
    tic_amt = ticket4
    total_amt = total_amt+tic_amt

#p5
if age_5 < 12:
    disco = ticket5 * 30/100 
    tic_amt = ticket5 - disco
    print(f'children : discount={disco} ticketamout={tic_amt}')
elif age_5 > 59:
    disco = ticket5 * 50/100
    tic_amt = ticket5 - disco
    print(f'adult: discount={disco} ticketamount={tic_amt}')   
else:
    tic_amt = ticket5
    total_amt = total_amt+tic_amt

total_amt = total_amt + tic_amt

print("Total amount =", total_amt)    


