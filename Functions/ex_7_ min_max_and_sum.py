def min_max_sum(some_list):
    list_of_integers = []
    for char in sequence:
        list_of_integers.append(int(char))
    min_number = min(list_of_integers)
    max_number = max(list_of_integers)
    sum_of_numbers = 0
    for num in list_of_integers:
        sum_of_numbers += num
    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_of_numbers}"


sequence = input().split()
print(min_max_sum(sequence))