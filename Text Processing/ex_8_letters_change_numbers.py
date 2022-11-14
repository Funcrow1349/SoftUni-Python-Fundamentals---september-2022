sequence = input().split()
total_sum = 0

for word in sequence:
    current_word = list(word)
    first_letter = current_word[0]
    last_letter = current_word[-1]
    number = []
    for digit in range(1, len(word) - 1):
        number.append(word[digit])
    number = int("".join(number))
    if first_letter.isupper():
        total_sum += number / (ord(first_letter) - 64)
    elif first_letter.islower():
        total_sum += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        total_sum -= (ord(last_letter) - 64)
    elif last_letter.islower():
        total_sum += (ord(last_letter) - 96)

print(f"{total_sum:.2f}")