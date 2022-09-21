phrase = input()
capitals = []


for letter in range(len(phrase)):
    if phrase[letter].isupper():
        capitals.append(letter)

print(capitals)

