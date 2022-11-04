initial_list = input().split()
bakery = {}

for index in range(0, len(initial_list), 2):
    key = initial_list[index]
    value = initial_list[index + 1]
    bakery[key] = int(value)

print(bakery)
