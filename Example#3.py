# Example 3 - Calculating Average

num_of_students = int(input("Enter the number of students: "))
count = num_of_students

sum = 0

while count > 0:
    mark = float(input(f"Enter mark {count - 1} remaining: "))
    sum += mark
    count -= 1 

average = sum/num_of_students

print(f"Your class average is {average}")