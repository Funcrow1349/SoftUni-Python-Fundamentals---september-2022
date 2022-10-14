list_numbers = list(map(int, input().split(", ")))
indices_of_even_numbers = [index for index in range(len(list_numbers)) if list_numbers[index] % 2 == 0]
print(indices_of_even_numbers)