# 4. WAP to print Armstrong number within a given range 
start = int(input("Enter starting number = "))
end = int(input("Enter ending number = "))

while start <= end:

    num = start
    original = num
    count = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** count
        num = num // 10

    if total == original:
        print(original)

    start = start + 1