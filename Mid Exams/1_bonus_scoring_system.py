import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus_points = 0
max_attendances = 0

for student in range(1, number_of_students + 1):
    count_of_attendances = int(input())
    total_bonus = (count_of_attendances / number_of_lectures) * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        max_attendances = count_of_attendances

print(f"Max Bonus: {math.ceil(max_bonus_points)}.")
print(f"The student has attended {max_attendances} lectures.")


