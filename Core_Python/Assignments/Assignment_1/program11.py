# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

amount = int(input('enter a amount='))
temp=amount

no500 = amount//500
amount = amount%500

no200 = amount//200
amount = amount%200

no100 = amount//100
amount = amount%100

no50= amount//50
amount = amount%50

no20 = amount//20
amount = amount%20

no10 = amount//10
amount = amount%10 

no5= amount//5
amount = amount%5

no2= amount//2
amount = amount%2 

no1 = amount // 1
amount = amount % 1  

print(f'amount={temp} 500 Notes={no500}  200 notes={no200} 100 notes={no100}  50 notess={no50}  20 notes={no20}  10 notes={no10} 5 notes={no5} 2 notes={no2}  1 notes={no1}')
total_notes = no500 + no200 + no100 + no50 + no20 + no10 + no5 + no2 + no1

print("total notes =", total_notes)
