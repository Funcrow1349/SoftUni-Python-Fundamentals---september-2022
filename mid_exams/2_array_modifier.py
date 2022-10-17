def swap(some_list, index1, index2):
    some_list[index1], some_list[index2] = some_list[index2], some_list[index1]
    return some_list


def multiply(some_list, index1, index2):
    some_list[index1] = some_list[index1] * some_list[index2]
    return some_list


def decrease(some_list):
    for index in range(len(some_list)):
        some_list[index] -= 1
    return some_list


list_of_integers = [int(num) for num in input().split()]
command = input().split()
while "end" not in command:
    if "decrease" in command:
        list_of_integers = decrease(list_of_integers)
    else:
        action = command[0]
        first_index = int(command[1])
        second_index = int(command[2])
        if action == "swap":
            list_of_integers = swap(list_of_integers, first_index, second_index)
        elif action == "multiply":
            list_of_integers = multiply(list_of_integers, first_index, second_index)
    command = input().split()

print(", ".join(str(item) for item in list_of_integers))

