import re

name_pattern = r"[^\s\,]"
damage_pattern = r"\-?\d+\.?\d+|\-?\d"
special_symbol_pattern = r"\*|\/"
all_symbols_pattern = r"[^\d\+\-\*\/\.]"
demons = input().split(",")
final_demons = []

for demon in demons:
    demon_name = "".join(re.findall(name_pattern, demon))
    damage = 0
    health = 0
    all_symbols = re.findall(all_symbols_pattern, demon_name)
    for symbol in all_symbols:
        health += ord(symbol)
    damage_values = re.findall(damage_pattern, demon_name)
    special_symbols = re.findall(special_symbol_pattern, demon_name)
    damage += sum(float(num) for num in damage_values)
    for symbol in special_symbols:
        if symbol == "*":
            damage = damage * 2
        elif symbol == "/":
            damage = damage / 2
    final_demons.append(f"{demon_name} - {health} health, {damage:.2f} damage")
for demon in sorted(final_demons):
    print(demon)
