def tribonacci_sequence(some_number):
    list_of_sums = [0, 0, 1]
    for num in range(1, some_number + 1):
        print(list_of_sums[-1], end=" ")
        list_of_sums.append(list_of_sums[-1] + list_of_sums[-2] + list_of_sums[-3])


number = int(input())
tribonacci_sequence(number)