import re

valid_links = []
pattern = r"(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"
line = input()
while line:
    matches = re.search(pattern, line)
    if matches:
        valid_links.append(matches[0])
    line = input()
for link in valid_links:
    print(link)