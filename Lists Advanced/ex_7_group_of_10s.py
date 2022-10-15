import math


def number_separator(some_sequence):
    final_output = []
    for decimal in range(1, int(math.ceil(int(max(some_sequence)) / 10)) + 1):
        decimal = decimal * 10
        current_list = [num for num in some_sequence if decimal - 10 < num <= decimal]
        final_output.append(f"Group of {decimal}'s: {current_list}")
    return final_output


sequence_of_numbers = [int(num) for num in input().split(", ")]
print("\n".join(number_separator(sequence_of_numbers)))

