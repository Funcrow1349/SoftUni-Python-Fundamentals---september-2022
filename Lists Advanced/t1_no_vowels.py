text = input()
filtered_text = [ch for ch in text if ch.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(filtered_text))