numbers = input().split()
abs_numbers = []

for num in numbers:
    current_number = abs(float(num))
    abs_numbers.append(current_number)

print(abs_numbers)

# numbers = list(map(float, input().split(' ')))
# result = [abs(num) for num in numbers]
# print(result)