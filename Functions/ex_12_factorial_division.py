def factorial_division(num1, num2):
    result_one = 1
    result_two = 1
    for m in range(1, num1):
        result_one += result_one * m
    for n in range(1, num2):
        result_two += result_two * n
    final_result = result_one // result_two
    return f"{final_result:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
