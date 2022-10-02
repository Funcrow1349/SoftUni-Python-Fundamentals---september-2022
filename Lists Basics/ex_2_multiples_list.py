factor = int(input())
count = int(input())
my_list = []

for num in range(factor, factor * count + 1, factor):
    my_list.append(num)

print(my_list)
