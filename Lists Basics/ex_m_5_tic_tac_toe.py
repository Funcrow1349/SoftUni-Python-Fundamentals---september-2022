first_line = input().split()
second_line = input().split()
third_line = input().split()
first_player_wins = False
second_player_wins = False

if first_line[0] == first_line[1] == first_line[2]:
    if first_line[0] == "1":
        first_player_wins = True
    elif first_line[0] == "2":
        second_player_wins = True
elif second_line[0] == second_line[1] == second_line[2]:
    if second_line[0] == "1":
        first_player_wins = True
    elif second_line[0] == "2":
        second_player_wins = True
elif third_line[0] == third_line[1] == third_line[2]:
    if third_line[0] == "1":
        first_player_wins = True
    elif third_line[0] == "2":
        second_player_wins = True
elif first_line[0] == second_line[0] == third_line[0]:
    if first_line[0] == "1":
        first_player_wins = True
    elif first_line[0] == "2":
        second_player_wins = True
elif first_line[1] == second_line[1] == third_line[1]:
    if first_line[1] == "1":
        first_player_wins = True
    elif first_line[1] == "2":
        second_player_wins = True
elif first_line[2] == second_line[2] == third_line[2]:
    if first_line[2] == "1":
        first_player_wins = True
    elif first_line[2] == "2":
        second_player_wins = True
elif first_line[0] == second_line[1] == third_line[2]:
    if first_line[0] == "1":
        first_player_wins = True
    elif first_line[0] == "2":
        second_player_wins = True
elif first_line[2] == second_line[1] == third_line[0]:
    if first_line[2] == "1":
        first_player_wins = True
    elif first_line[2] == "2":
        second_player_wins = True
if first_player_wins:
    print("First player won")
elif second_player_wins:
    print("Second player won")
else:
    print("Draw!")


