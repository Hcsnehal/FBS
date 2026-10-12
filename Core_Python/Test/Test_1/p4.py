
area = float(input("Enter area of one wall = "))

interior_cost = float(input("Enter interior painting cost per unit area = "))
exterior_cost = float(input("Enter exterior painting cost per unit area = "))

interior_area = area * 7
exterior_area = area * 6

total_interior_cost = interior_area * interior_cost
total_exterior_cost = exterior_area * exterior_cost

total_cost = total_interior_cost + total_exterior_cost

print("Interior painting cost =", total_interior_cost)
print("Exterior painting cost =", total_exterior_cost)
print("Total painting cost =", total_cost)
