num = int(input("Enter number = "))

original = num
count = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** count
    num = num // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
   