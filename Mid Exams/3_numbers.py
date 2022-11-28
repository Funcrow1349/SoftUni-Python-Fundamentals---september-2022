line_of_integers = [int(num) for num in input().split()]
average_number = sum(line_of_integers) / len(line_of_integers)
bigger_numbers = 5
list_of_bigger_numbers = []
final_list = []

for num in line_of_integers:
    if num > average_number:
        list_of_bigger_numbers.append(num)

while len(final_list) < 5:
    if len(list_of_bigger_numbers) == 0:
        break
    final_list.append(max(list_of_bigger_numbers))
    list_of_bigger_numbers.remove(max(list_of_bigger_numbers))

if len(final_list) == 0:
    print("No")
else:
    print(" ".join(str(num) for num in final_list))





