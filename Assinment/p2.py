# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.


students = int(input("Enter number of students = "))

total_percentage = 0
i = 1

while i <= students:

    print("Enter marks for student", i)

    total = 0
    j = 1

    while j <= 5:
        marks = int(input("Enter marks = "))
        total = total + marks
        j = j + 1

    percentage = total / 5
    print("Percentage =", percentage)

    total_percentage = total_percentage + percentage
    i = i + 1

average = total_percentage / students

print("Average percentage =", average)