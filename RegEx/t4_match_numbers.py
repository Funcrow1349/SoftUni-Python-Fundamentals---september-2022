import re
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
raw_input = input()
matches = re.finditer(pattern, raw_input)
for match in matches:
    print(match.group(), end=" ")