command = input().split(" ")
team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
team_a_length = len(team_a)
team_b_length = len(team_b)
game_terminated = False

for char in command:
    if char not in team_a and char not in team_b:
        continue
    if "A" in char:
        team_a.remove(char)
        team_a_length -= 1
    else:
        team_b.remove(char)
        team_b_length -= 1
    if team_a_length < 7 or team_b_length < 7:
        game_terminated = True
        break

print(f"Team A - {team_a_length}; Team B - {team_b_length}")
if game_terminated:
    print(f"Game was terminated")