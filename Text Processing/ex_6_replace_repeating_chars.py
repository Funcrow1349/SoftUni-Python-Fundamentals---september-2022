sequence_of_letters = input()
last_letter = ""
for letter in sequence_of_letters:
    if letter != last_letter:
        print(letter, end="")
        last_letter = letter