# 3. Convert distant given in feet and inches into meter and centimeter.

feet = float(input('enter feet :'))
inches = float(input('enter inches: '))

total_meter = (feet * 0.3048) + (inches * 0.0254)
meter = int(total_meter)
centimeter = (total_meter - meter) * 100

print(f'total meter is {meter} and centimeters is {centimeter}')
