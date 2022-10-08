def even_nums(some_list):
    list_of_even_numbers = []
    for char in some_list:
        if int(char) % 2 == 0:
            list_of_even_numbers.append(int(char))
    return list_of_even_numbers


list_of_numbers = input().split()
print(even_nums(list_of_numbers))