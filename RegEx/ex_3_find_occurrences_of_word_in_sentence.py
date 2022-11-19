import re
sentence = input()
key_word = input()
pattern = fr"{key_word}\b"
matches = re.findall(pattern, sentence, re.IGNORECASE)
print(len(matches))