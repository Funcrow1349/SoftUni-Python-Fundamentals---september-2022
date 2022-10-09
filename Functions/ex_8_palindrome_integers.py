def palindrome_checker(some_list):
    for num in some_list:
        num = list(num)
        reversed_list = []
        for digit in range(len(num) -1, -1, -1):
            reversed_list.append(num[digit])
        if num == reversed_list:
            print(True)
        else:
            print(False)


list_of_integers = input().split(", ")
palindrome_checker(list_of_integers)