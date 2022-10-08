def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum, num3):
    return sum - num3


def add_and_subtract(num1, num2, num3):
    sum_of_first_and_second = sum_numbers(num1, num2)
    result = subtract(sum_of_first_and_second, num3)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))