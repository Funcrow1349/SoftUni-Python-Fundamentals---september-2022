materials = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
needed_mats = 250
while not obtained:
    mats = input().split()
    for index in range(0, len(mats), 2):
        current_material = mats[index + 1].lower()
        current_quantity = int(mats[index])
        if current_material not in materials.keys():
            materials[current_material] = 0
        materials[current_material] += current_quantity
        if materials["shards"] >= needed_mats:
            materials["shards"] -= needed_mats
            print("Shadowmourne obtained!")
            obtained = True
        elif materials["fragments"] >= needed_mats:
            materials["fragments"] -= needed_mats
            print("Valanyr obtained!")
            obtained = True
        elif materials["motes"] >= needed_mats:
            materials["motes"] -= needed_mats
            print("Dragonwrath obtained!")
            obtained = True
        if obtained:
            break

for material, quantity in materials.items():
    print(f"{material}: {quantity}")