import re
raw_text = input()
digit_pattern = r"\d"
emoji_pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})(\1)"
cool_emojis = []

all_digits = re.findall(digit_pattern, raw_text)
cool_threshold = int(all_digits[0])
for digit in range(1, len(all_digits)):
    cool_threshold *= int(all_digits[digit])

all_emojis = re.findall(emoji_pattern, raw_text)
for emoji in all_emojis:
    total_coolness = 0
    for letter in emoji[1]:
        total_coolness += ord(letter)
    if total_coolness >= cool_threshold:
        cool_emojis.append("".join(emoji))
print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)


