# 2. Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)


p = float(input("Enter principal = "))
r = float(input("Enter rate = "))
t = float(input("Enter time = "))

SI = (p * r * t) / 100
print("Simple Interest =", SI)
