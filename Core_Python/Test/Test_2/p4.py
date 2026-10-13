# 4. Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.


length = float(input("Enter length of the wall: "))
height = float(input("Enter height of the wall: "))
cost = float(input("Enter painting cost per square meter: "))

area = 4 * length * height
total_cost = area * cost
print("Total area of four walls=", area)
print("Total cost of painting=", total_cost)
