countries = input().split(", ")
cities = input().split(", ")
zipped = list(zip(countries, cities))
capitals = {}

for country, city in zipped:
    capitals[country] = city

for country, city in capitals.items():
    print(f"{country} -> {city}")