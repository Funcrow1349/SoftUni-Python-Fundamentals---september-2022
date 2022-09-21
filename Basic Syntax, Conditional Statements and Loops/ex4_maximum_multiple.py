divisor = int(input())
boundary = int(input())
maximum_number = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        maximum_number = i

print(maximum_number)
