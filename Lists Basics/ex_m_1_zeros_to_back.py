string_of_numbers = input().split(", ")
list_of_integers = []
zeroes = 0
for char in string_of_numbers:
    list_of_integers.append(int(char))

for num in range(len(list_of_integers) -1, -1, -1):
    if list_of_integers[num] == 0:
        list_of_integers.remove(list_of_integers[num])
        zeroes += 1
for zero in range(zeroes):
    list_of_integers.append(0)

print(list_of_integers)
