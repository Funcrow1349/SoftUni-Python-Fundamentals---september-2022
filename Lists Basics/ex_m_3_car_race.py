sequence_of_numbers = input().split()
sequence_of_times = []
for num in sequence_of_numbers:
    sequence_of_times.append(int(num))
left_car_time = 0
right_car_time = 0
for time in range((len(sequence_of_times) -1) // 2):
    left_car_time += sequence_of_times[time]
    if sequence_of_times[time] == 0:
        left_car_time = left_car_time * 0.80
for time in range((len(sequence_of_times) - 1), (len(sequence_of_times) - 1) // 2, -1):
    right_car_time += sequence_of_times[time]
    if sequence_of_times[time] == 0:
        right_car_time = right_car_time * 0.80
if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")