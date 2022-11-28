import math

first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
nr_of_students = int(input())
total_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
total_hours = 0

while nr_of_students > 0:
    nr_of_students -= total_efficiency
    total_hours += 1
    if total_hours % 4 == 0:
        total_hours += 1

print(f"Time needed: {total_hours}h.")
