contests = {}
while True:
    command = input()
    if command == "no more time":
        break
    current_entry = command.split(" -> ")
    current_subject = current_entry[1]
    current_student = current_entry[0]
    current_points = int(current_entry[2])
    if current_subject not in contests.keys():
        contests[current_subject] = {}
        if current_student not in contests[current_subject].keys():
            contests[current_subject][current_student] = current_points
        else:
            if current_points > contests[current_subject][current_student]:
                contests[current_subject][current_student] = current_points
    else:
        if current_student not in contests[current_subject].keys():
            contests[current_subject][current_student] = current_points
        else:
            if current_points > contests[current_subject][current_student]:
                contests[current_subject][current_student] = current_points
for contest, participant in contests.items():
    sorted_by_points = {k: v for k, v in sorted(participant.items(), key=lambda item: (-item[1], item[0]))}
    print(f"{contest}: {len(sorted_by_points.keys())} participants")
    position = 1
    for student in sorted_by_points.keys():
        print(f"{position}. {student} <::> {sorted_by_points[student]}")
        position += 1
print("Individual standings:")
individual_standings = {}
for contest, participant in contests.items():
    for student, points in participant.items():
        if student not in individual_standings.keys():
            individual_standings[student] = 0
        individual_standings[student] += points
final_individual_standings = {k: v for k, v in sorted(individual_standings.items(), key=lambda item: (-item[1], item[0]))}
student_position = 1
for student, points in final_individual_standings.items():
    print(f"{student_position}. {student} -> {points}")
    student_position += 1

