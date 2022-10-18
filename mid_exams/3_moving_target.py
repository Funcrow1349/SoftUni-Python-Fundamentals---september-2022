def moving_targets(some_sequence):
    while True:
        command = input()
        if command == "End":
            break
        command = list(command.split())
        action = command[0]
        index = int(command[1])
        power_value_radius = int(command[2])
        if action == "Shoot":
            if 0 <= index < len(some_sequence):
                some_sequence[index] -= power_value_radius
                if some_sequence[index] <= 0:
                    some_sequence.remove(some_sequence[index])
        elif action == "Add":
            if 0 <= index < len(some_sequence):
                some_sequence.insert(index, power_value_radius)
            else:
                print("Invalid placement!")
        elif action == "Strike":
            max_index = index + power_value_radius
            min_index = index - power_value_radius
            if min_index < 0 or max_index >= len(some_sequence):
                print("Strike missed!")
            else:
                for value in range(max_index, min_index - 1, - 1):
                    some_sequence.remove(some_sequence[value])
    some_sequence = "|".join(str(num) for num in some_sequence)
    return some_sequence


sequence_of_targets = [int(num) for num in input().split()]
print(moving_targets(sequence_of_targets))
