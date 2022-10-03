sequence_of_numbers = input().split()
phrase = input()
phrase = list(phrase)
message = []

for number in sequence_of_numbers:
    current_number = list(number)
    index = - len(phrase)
    for symbol in current_number:
        digit = int(symbol)
        index += digit
    message.append(phrase[index])
    phrase.remove(phrase[index])
print("".join(message))

