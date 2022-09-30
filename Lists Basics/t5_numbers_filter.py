number_of_lines = int(input())
integers = []
filtered_integers = []

for num in range(number_of_lines):
    current_number = int(input())
    integers.append(current_number)

command = input()

if command == "even":
    for num in integers:
        if num % 2 == 0:
            filtered_integers.append(num)
elif command == "odd":
    for num in integers:
        if num % 2 != 0:
            filtered_integers.append(num)
elif command == "negative":
    for num in integers:
        if num < 0:
            filtered_integers.append(num)
elif command == "positive":
    for num in integers:
        if num >= 0:
            filtered_integers.append(num)

print(filtered_integers)
