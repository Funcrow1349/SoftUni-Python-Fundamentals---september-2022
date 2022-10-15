first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []

for char in first_sequence:
    for ch in second_sequence:
        if char in ch:
            substrings.append(char)
            break
print(substrings)


# alternative solution:
# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]
# print(substrings)