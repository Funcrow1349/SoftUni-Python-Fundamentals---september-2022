number_of_people = int(input())
elevator_capacity = int(input())

courses = number_of_people / elevator_capacity

if number_of_people % elevator_capacity != 0:
    courses += 1

print(int(courses))