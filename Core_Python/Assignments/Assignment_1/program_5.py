#5. WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input('enter cose price of the book :'))
discount = float(input('enter discount percentage of book :'))

discount_amount = (cost_price*discount)/100
selling_price  = cost_price - discount

print(f'discount amount is {discount_amount}')
print(f'selling price is {selling_price}')

