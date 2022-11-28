import re
places_on_the_map = input()
pattern = r"(\=|\/)([A-Z][a-zA-Z][a-zA-Z]+)\1"
locations = re.findall(pattern, places_on_the_map)
location_list = []
travel_points = 0
for point in locations:
    travel_points += len(point[1])
for location in locations:
    location_list.append(location[1])
print(f"Destinations: {', '.join(location_list)}")
print(f"Travel Points: {travel_points}")