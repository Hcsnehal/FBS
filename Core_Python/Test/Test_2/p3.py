# 3. A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

import math
radius = 34
length = 56
breadth = 20
cost_per_meter = 35
times = 5

circle = 2 * math.pi * radius
rectangle = 2 * (length + breadth)
perimeter = circle + rectangle
wire = perimeter * times
cost = wire * cost_per_meter

print("Total perimeter of field:", round(perimeter, 2), "m")
print("Total wire required:", round(wire, 2), "m")
print("Total cost of fencing: Rs.", round(cost, 2))
