sequence_of_steps = [int(num) for num in input().split()]
sum_of_removed_elements = 0
while len(sequence_of_steps) > 0:
    current_index = int(input())
    if current_index < 0:
        removed_item = sequence_of_steps.pop(0)
        sequence_of_steps.insert(0, sequence_of_steps[-1])
        for num in range(len(sequence_of_steps)):
            if sequence_of_steps[num] <= removed_item:
                sequence_of_steps[num] += removed_item
            else:
                sequence_of_steps[num] -= removed_item
        sum_of_removed_elements += removed_item
    elif current_index >= len(sequence_of_steps):
        removed_item = sequence_of_steps.pop()
        sequence_of_steps.append(sequence_of_steps[0])
        for num in range(len(sequence_of_steps)):
            if sequence_of_steps[num] <= removed_item:
                sequence_of_steps[num] += removed_item
            else:
                sequence_of_steps[num] -= removed_item
        sum_of_removed_elements += removed_item
    else:
        removed_item = sequence_of_steps.pop(current_index)
        for num in range(len(sequence_of_steps)):
            if sequence_of_steps[num] <= removed_item:
                sequence_of_steps[num] += removed_item
            else:
                sequence_of_steps[num] -= removed_item
        sum_of_removed_elements += removed_item
print(sum_of_removed_elements)
