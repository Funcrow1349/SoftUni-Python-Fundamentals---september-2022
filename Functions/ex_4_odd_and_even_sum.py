def odd_even_sums(num):
    evens = 0
    odds = 0
    for digit in num:
        if int(digit) % 2 == 0:
            evens += int(digit)
        else:
            odds += int(digit)
    return f"Odd sum = {odds}, Even sum = {evens}"


single_number = input()
print(odd_even_sums(single_number))