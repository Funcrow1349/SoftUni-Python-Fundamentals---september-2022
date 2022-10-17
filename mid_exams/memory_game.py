sequence_of_elements = input().split()
command = input().split()
nr_of_turns = 0

while len(command) > 1:
    first_index = int(command[0])
    second_index = int(command[1])
    if first_index == second_index or (first_index < 0 or second_index < 0 or first_index >= len(sequence_of_elements)
                                       or second_index >= len(sequence_of_elements)):
        print("Invalid input! Adding additional elements to the board")
        nr_of_turns += 1
        middle_of_the_sequence = len(sequence_of_elements) // 2
        sequence_of_elements.insert(middle_of_the_sequence, f"-{nr_of_turns}a")
        sequence_of_elements.insert(middle_of_the_sequence, f"-{nr_of_turns}a")
        command = input().split()
        continue
    if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[second_index]}!")
        char = sequence_of_elements[first_index]
        nr_of_turns += 1
        for index in range(len(sequence_of_elements) - 1, -1, -1):
            if sequence_of_elements[index] == char:
                sequence_of_elements.remove(sequence_of_elements[index])
    else:
        nr_of_turns += 1
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {nr_of_turns} turns!")
        break
    command = input().split()
if len(sequence_of_elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))
