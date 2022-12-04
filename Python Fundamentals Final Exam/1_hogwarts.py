spell = input()
while True:
    command = input().split()
    if command[0] == "Abracadabra":
        break
    elif command[0] == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command[0] == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif command[0] == "Illusion":
        index, letter = int(command[1]), command[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif command[0] == "Divination":
        first_string, second_string = command[1], command[2]
        if first_string in spell:
            spell = spell.replace(first_string, second_string)
            if spell:
                print(spell)
    elif command[0] == "Alteration":
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            if spell:
                print(spell)
    else:
        print("The spell did not work!")
