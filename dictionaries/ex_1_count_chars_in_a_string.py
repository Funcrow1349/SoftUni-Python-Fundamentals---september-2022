string = list(input())
character_dictionary = {}

for char in string:
    if char != " ":
        if char not in character_dictionary:
            character_dictionary[char] = 0
        character_dictionary[char] += 1

for key, value in character_dictionary.items():
    print(f"{key} -> {value}")