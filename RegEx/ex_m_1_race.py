import re

list_of_participants = input().split(", ")
total_distances = {}
names_pattern = r"([a-zA-Z])"
digits_pattern = r"\d"
while True:
    command = input()
    if command == "end of race":
        break
    name = "".join(re.findall(names_pattern, command))
    distance = re.findall(digits_pattern, command)
    if name in list_of_participants:
        if name not in total_distances.keys():
            total_distances[name] = 0
        total_distances[name] += sum(int(km) for km in distance)
sorted_total_distances = {k: v for k, v in sorted(total_distances.items(), key=lambda item: item[1], reverse=True)}
final_standings = []
for racer in sorted_total_distances:
    final_standings.append(racer)
print(f"1st place: {final_standings[0]}")
print(f"2nd place: {final_standings[1]}")
print(f"3rd place: {final_standings[2]}")