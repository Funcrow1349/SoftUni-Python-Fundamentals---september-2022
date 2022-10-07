numbers = list(map(float, input().split()))
rounded_numbers = []
for num in numbers:
    rounded_numbers.append(round(num))

print(rounded_numbers)