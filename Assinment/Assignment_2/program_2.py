# 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
# 1c=32f
# formulae to convert temp form celcius to fehrenheit : F = (C × 9/5) + 32

celsius = float(input('Enter a temp in celcius :'))
Fahrenheit = (celsius * 9 / 5) + 32
print(f'temperature in Fahrenheit {Fahrenheit}')