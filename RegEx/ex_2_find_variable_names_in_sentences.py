import re
pattern = r"\b_([A-Za-z0-9]+)\b"
line = input()
result = re.findall(pattern, line)
print(",".join(result))