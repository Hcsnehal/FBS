# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passengers = int(input("Enter number of passengers = "))
ticket = float(input("Enter ticket cost = "))

total = 0
i = 1

while i <= passengers:

    age = int(input("Enter age = "))

    if age < 12:
        ticket_cost = ticket - (ticket * 30 / 100)

    elif age > 59:
        ticket_cost = ticket - (ticket * 50 / 100)

    else:
        ticket_cost = ticket

    total = total + ticket_cost
    i = i + 1

print("Total ticket amount =", total)