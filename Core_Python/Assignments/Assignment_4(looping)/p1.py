# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


correct_id = "firstbit_solution"
correct_password = "8189"

attempt = 1

while attempt <= 3:
    userid = input("Enter user ID = ")
    password = input("Enter password = ")

    if userid == correct_id and password == correct_password:
        print("Login successful...")
        break
    else:
        print("Incorrect ID or password")
        attempt = attempt + 1

if attempt > 3:
    print("you have only 3 attemts...")