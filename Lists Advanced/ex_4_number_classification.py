def positive_numbers(some_list):
    return [num for num in some_list if int(num) >= 0]


def negative_numbers(some_list):
    return [num for num in some_list if int(num) < 0]


def even_numbers(some_list):
    return [num for num in some_list if int(num) % 2 == 0]


def odd_numbers(some_list):
    return [num for num in some_list if int(num) % 2 != 0]


numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")
