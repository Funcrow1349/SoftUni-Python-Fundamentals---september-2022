import re
number_of_messages = int(input())
pattern = r"[sStTaArR]"
decrypted_messages = []
for message in range(number_of_messages):
    encrypted_message = input()
    decryption_key = len(re.findall(pattern, encrypted_message))
    decrypted_message = list(encrypted_message)
    for index in range(len(encrypted_message)):
        decrypted_message[index] = chr(ord(encrypted_message[index]) - decryption_key)
    decrypted_messages.append("".join(decrypted_message))
pattern_two = r"\@([A-Z][a-z]+)[^\@\-\!\:\>]*?:(\d+)[^\@\-\!\:\>]*?!([AD])![^\@\-\!\:\>]*?->(\d+)"
attacked_planets = []
destroyed_planets = []
for message in decrypted_messages:
    matches = re.search(pattern_two, message)
    if matches:
        planet_name, population, attack_type, soldier_count = matches.groups()
        if attack_type == "A":
            attacked_planets.append(planet_name)
        else:
            destroyed_planets.append(planet_name)
print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
