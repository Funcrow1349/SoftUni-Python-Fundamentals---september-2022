number_of_lines = int(input())
total_sum = 0

for l in range(number_of_lines):
    current_symbol = ord(input())
    total_sum += current_symbol

print(f"The sum equals: {total_sum}")