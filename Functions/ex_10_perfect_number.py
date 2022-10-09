def perfection_check(some_num):
    divisors_sum = 0
    for divisor in range(1, some_num // 2 + 1):
        if some_num % divisor == 0:
            divisors_sum += divisor
    if divisors_sum == some_num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfection_check(number))