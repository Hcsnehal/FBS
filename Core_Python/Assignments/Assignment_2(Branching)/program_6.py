# 6. Write a program to calculate profit or loss.

cost_price = float(input('enter a cost price..'))
selling_price = float(input('enter a selling price..'))

if(cost_price <= 0 or selling_price <= 0):
    print('invalid input , price cannot be negetive or an zero....')
elif(selling_price > cost_price):
    profit=selling_price - cost_price
    print(f'profit={profit}')   
elif(cost_price > selling_price):
    loss=cost_price-selling_price
    print(f'loss={loss}')    
else:
    print('no profit, no loss.....')     

