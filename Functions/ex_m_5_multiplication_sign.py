def positive_or_negative(n1, n2, n3):
    negative_count = 0
    zeroes = 0
    if n1 != 0 and n2 != 0 and n3 != 0:
        if n1 < 0:
            negative_count += 1
        if n2 < 0:
            negative_count += 1
        if n3 < 0:
            negative_count += 1
        if negative_count == 1 or negative_count == 3:
            return "negative"
        return "positive"
    return "zero"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(positive_or_negative(first_number, second_number, third_number))