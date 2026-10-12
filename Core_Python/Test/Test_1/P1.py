
len= float(input("Enter length = "))
breadth = float(input("Enter breadth = "))
re = float(input("Enter radius = "))
arearect = len * breadth 
areasemi = (3.14 * re * re) / 2
total_area = arearect + areasemi
perimeter = len + (2 * breadth) + (3.14 * re)

print("Area of figure =", total_area)
print("Perimeter of figure =", perimeter)
