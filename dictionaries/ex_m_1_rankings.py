contest_passwords = {}
student_scores = {}
while True:
    command = input()
    if command == "end of contests":
        break
    current_contest = command.split(":")
    contest = current_contest[0]
    password = current_contest[1]
    contest_passwords[contest] = password
while True:
    command = input()
    if command == "end of submissions":
        break
    current_submission = command.split("=>")
    current_contest_type = current_submission[0]
    current_contest_password = current_submission[1]
    current_student = current_submission[2]
    current_points = int(current_submission[3])
    if current_contest_type in contest_passwords.keys():
        if current_contest_password == contest_passwords[current_contest_type]:
            if current_contest_type not in student_scores.keys():
                student_scores[current_contest_type] = {}
            if current_student not in student_scores[current_contest_type].keys():
                student_scores[current_contest_type][current_student] = current_points
            else:
                if current_points > student_scores[current_contest_type][current_student]:
                    student_scores[current_contest_type][current_student] = current_points
best_candidate = {}
for key, value in student_scores.items():
    for student, points in value.items():
        if student not in best_candidate.keys():
            best_candidate[student] = 0
        best_candidate[student] += points
highest_score = [" ", 0]
for student, points in best_candidate.items():
    if points > highest_score[1]:
        highest_score[0] = student
        highest_score[1] = points
print(f"Best candidate is {highest_score[0]} with total {highest_score[1]} points.")
print("Ranking:")
sorted_dict = {}
for course, scores in student_scores.items():
    for student in scores.keys():
        if student not in sorted_dict.keys():
            sorted_dict[student] = {}
            if course not in sorted_dict[student].keys():
                sorted_dict[student][course] = 0
            sorted_dict[student][course] = scores[student]
        sorted_dict[student][course] = scores[student]
sorted_names = dict(sorted(sorted_dict.items()))
for student_name, courses_scores in sorted_names.items():
    sorted_scores = {}
    print(f"{student_name}")
    for course_name, course_points in courses_scores.items():
        sorted_scores[course_name] = course_points
    final_sorted_scores = {k: v for k, v in sorted(sorted_scores.items(), key=lambda item: item[1], reverse=True)}
    for contest, points in final_sorted_scores.items():
        print(f"#  {contest} -> {points}")










