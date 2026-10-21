# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

D = [2000, 500, 200, 100, 50, 20, 10, 5]
amt = int(input('enter amount='))
count = 0
for note in D:
    n = amt // note
    if n > 0:
        print(note, ":", n)
        count += n
        amt = amt % note
print('number of notes=',count)