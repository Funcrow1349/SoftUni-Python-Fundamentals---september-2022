import re
dates = input()
search_pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4}\b)"
results = re.findall(search_pattern, dates)
for result in results:
    print(f"Day: {result[0]}, Month: {result[2]}, Year: {result[3]}")