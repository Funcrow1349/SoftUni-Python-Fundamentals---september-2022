starting_symbol = input()
final_symbol = input()
start = ord(starting_symbol)
end = ord(final_symbol)
sequence = input()
total_sum = 0

for char in sequence:
    if start < ord(char) < end:
        total_sum += ord(char)

print(total_sum)
