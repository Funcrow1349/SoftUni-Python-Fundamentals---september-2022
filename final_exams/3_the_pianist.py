number_of_pieces = int(input())
pieces = {}
for entry in range(number_of_pieces):
    current_entry = input().split("|")
    piece = current_entry[0]
    composer = current_entry[1]
    key = current_entry[2]
    pieces[piece] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        break
    instructions = command.split("|")
    action = instructions[0]
    if action == "Add":
        piece_to_add = instructions[1]
        composer_to_add = instructions[2]
        key_to_add = instructions[3]
        if piece_to_add not in pieces.keys():
            pieces[piece_to_add] = [composer_to_add, key_to_add]
            print(f"{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!")
        else:
            print(f"{piece_to_add} is already in the collection!")
    elif action == "Remove":
        piece_to_remove = instructions[1]
        if piece_to_remove in pieces.keys():
            del pieces[piece_to_remove]
            print(f"Successfully removed {piece_to_remove}!")
        else:
            print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
    elif action == "ChangeKey":
        piece_to_check = instructions[1]
        new_key = instructions[2]
        if piece_to_check not in pieces.keys():
            print(f"Invalid operation! {piece_to_check} does not exist in the collection.")
        else:
            pieces[piece_to_check][1] = new_key
            print(f"Changed the key of {piece_to_check} to {new_key}!")
for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")