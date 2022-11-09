season_ranking = {}
while True:
    command = input()
    if command == "Season end":
        break
    if "vs" in command:
        current_duel = command.split(" vs ")
        player_one = current_duel[0]
        player_two = current_duel[1]
        if player_one in season_ranking.keys() and player_two in season_ranking.keys():
            player_defeated = False
            for position_one in season_ranking[player_one].keys():
                if player_defeated:
                    break
                for position_two in season_ranking[player_two].keys():
                    if player_defeated:
                        break
                    if position_one == position_two:
                        if season_ranking[player_one][position_one] > season_ranking[player_two][position_two]:
                            del season_ranking[player_two]
                            player_defeated = True
                        elif season_ranking[player_one][position_one] < season_ranking[player_two][position_two]:
                            del season_ranking[player_one]
                            player_defeated = True
    else:
        current_entry = command.split(" -> ")
        current_player = current_entry[0]
        current_position = current_entry[1]
        current_skill = int(current_entry[2])
        if current_player not in season_ranking.keys():
            season_ranking[current_player] = {}
            if current_position not in season_ranking[current_player].keys():
                season_ranking[current_player][current_position] = current_skill
            else:
                if current_skill > season_ranking[current_player][current_position]:
                    season_ranking[current_player][current_position] = current_skill
        else:
            if current_position not in season_ranking[current_player].keys():
                season_ranking[current_player][current_position] = current_skill
            else:
                if current_skill > season_ranking[current_player][current_position]:
                    season_ranking[current_player][current_position] = current_skill
season_ranking_ordered = {}
for player, game in season_ranking.items():
    for position, skill in game.items():
        if player not in season_ranking_ordered.keys():
            season_ranking_ordered[player] = 0
        season_ranking_ordered[player] += skill
season_ranking_ordered = {k: v for k, v in sorted(season_ranking_ordered.items(), key=lambda item: (-item[1], item[0]))}
for player, points in season_ranking_ordered.items():
    print(f"{player}: {points} skill")
    player_positions = {k: v for k, v in sorted(season_ranking[player].items(), key=lambda item: (-item[1], item[0]))}
    for position, skill in player_positions.items():
        print(f"- {position} <::> {skill}")
