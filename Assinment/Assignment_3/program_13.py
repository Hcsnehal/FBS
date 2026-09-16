# Write a program to input electricity unit charges and calculate total electricity bill:

# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill







ele_unit=int(input('enter a unit='))

if ele_unit <= 50:
    Bill=ele_unit * 0.50 
    

elif ele_unit > 50 and ele_unit <= 150:
    Bill = ele_unit * 0.75 
   

elif ele_unit > 150 and ele_unit <= 250:  #150-250
    Bill =ele_unit * 0.20 

elif ele_unit >= 250:
    Bill=ele_unit*1.50 

subcharges=Bill*20/100    
total_Bill=Bill+subcharges
   


 
