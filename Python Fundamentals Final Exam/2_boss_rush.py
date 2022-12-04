import re
number_of_inputs = int(input())
pattern = r"\|([A-Z]{4,})\|\:\#([a-zA-Z]+ [a-zA-Z]+)\#"
for current_entry in range(number_of_inputs):
    entry = input()
    matches = re.findall(pattern, entry)
    if matches:
        print(f"{matches[0][0]}, The {matches[0][1]}")
        print(f">> Strength: {len(matches[0][0])}")
        print(f">> Armor: {len(matches[0][1])}")
    else:
        print("Access denied!")