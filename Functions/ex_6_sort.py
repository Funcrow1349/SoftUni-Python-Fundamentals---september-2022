def list_sorting(some_list):
    list_of_numbers = []
    for char in some_list:
        list_of_numbers.append(int(char))
    sorted_list = sorted(list_of_numbers)
    return sorted_list


sequence = input().split()
print(list_sorting(sequence))