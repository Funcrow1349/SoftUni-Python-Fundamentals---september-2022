def target_practice(some_sequence):
    command = input()
    targets_shot = 0
    while command != "End":
        index = int(command)
        if index >= len(some_sequence) or index < 0:
            command = input()
            continue
        current_value = some_sequence[index]
        if current_value == -1:
            command = input()
            continue
        some_sequence[index] = -1
        targets_shot += 1
        for num in range(len(some_sequence)):
            if some_sequence[num] == -1:
                continue
            else:
                if some_sequence[num] <= current_value:
                    some_sequence[num] += current_value
                else:
                    some_sequence[num] -= current_value
        command = input()
    some_sequence = " ".join(str(item) for item in some_sequence)
    return f"Shot targets: {targets_shot} -> {some_sequence}"


sequence_of_integers = [int(num) for num in input().split()]
print(target_practice(sequence_of_integers))


