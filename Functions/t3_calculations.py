current_operator = input()
first_number = int(input())
second_number = int(input())


def calculator(operator, first, second):
    if "add" in operator:
        return first + second
    elif "subtract" in operator:
        return first - second
    elif "multiply" in operator:
        return first * second
    elif "divide" in operator:
        return int(first // second)


result = calculator(current_operator, first_number, second_number)
print(result)