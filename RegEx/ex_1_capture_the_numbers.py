import re

pattern = r"\d+"
line = input()
while line:
    matches = re.findall(pattern, line)
    if matches:
        print(" ".join(matches), end=" ")
    line = input()
