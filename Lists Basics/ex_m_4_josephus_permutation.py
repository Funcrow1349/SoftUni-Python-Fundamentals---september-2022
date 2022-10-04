people_numbers = input().split()
k_step = int(input())
people_killed = []
counter = 0
index = 0
while len(people_numbers) > 0:
    counter += 1
    if counter % k_step == 0:
        people_killed.append(people_numbers.pop(index))
    else:
        index += 1
    if index >= len(people_numbers):
        index = 0

print(str(people_killed).replace(' ', '').replace('\'', ''))