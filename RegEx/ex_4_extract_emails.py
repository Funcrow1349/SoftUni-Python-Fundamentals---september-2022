import re

pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b"
line = input()
matches = re.findall(pattern, line)
for match in matches:
    print(match[0])