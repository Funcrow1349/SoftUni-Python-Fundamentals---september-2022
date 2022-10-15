number_of_rooms = int(input())
free_chairs = 0
for room in range(1, number_of_rooms + 1):
    current_room = input().split()
    nr_of_chairs = len(current_room[0])
    visitors = int(current_room[1])
    if visitors > nr_of_chairs:
        chairs_needed = visitors - nr_of_chairs
        free_chairs -= chairs_needed
        print(f"{chairs_needed} more chairs needed in room {room}")
    else:
        free_chairs += nr_of_chairs - visitors
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")

# alternative solution:
# def check_the_rooms(numbers_of_rooms):
#     total_free_chairs = 0
#     total_needed_chairs = 0
#     for room in range(1, numbers_of_rooms + 1):
#         free_chairs, visitors = input().split()
#         difference = len(free_chairs) - int(visitors)
#         if difference >= 0:
#             total_free_chairs += difference
#         else:
#             total_needed_chairs += abs(difference)
#             print(f"{abs(difference)} more chairs needed in room {room}")
#     return total_free_chairs, total_needed_chairs
#
#
# number_of_rooms = int(input())
# free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
# if free_chairs >= needed_chairs:
#     print(f"Game On, {free_chairs} free chairs left")