import re
text_string = input()
pattern = r"(\@|\#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)"
pairs = re.findall(pattern, text_string)
matching_words = []


for pair in pairs:
    first_word = pair[1]
    second_word = pair[3]
    if first_word == second_word[::-1]:
        matching_words.append(f"{first_word} <=> {second_word}")

if not pairs:
    print("No word pairs found!")
else:
    print(f"{len(pairs)} word pairs found!")
if not matching_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(f"{', '.join(matching_words)}")