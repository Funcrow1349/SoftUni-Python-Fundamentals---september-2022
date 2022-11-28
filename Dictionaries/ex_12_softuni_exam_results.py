exam_results = {}
submissions = {}
banned_students = []
while True:
    command = input()
    if command == "exam finished":
        break
    elif "banned" in command:
        current_ban = command.split("-")
        banned_user = current_ban[0]
        if banned_user in exam_results.keys():
            banned_students.append(banned_user)
            del exam_results[banned_user]
        continue
    current_entry = command.split("-")
    student = current_entry[0]
    course = current_entry[1]
    points = int(current_entry[2])
    if course not in submissions.keys():
        submissions[course] = 0
    submissions[course] += 1
    if student not in exam_results.keys() and student not in banned_students:
        exam_results[student] = points
    if points > exam_results[student]:
        exam_results[student] = points
if len(banned_students) < len(exam_results.keys()):
    print("Results:")
for name, result in exam_results.items():
    print(f"{name} | {result}")
print("Submissions:")
for language, submits in submissions.items():
    print(f"{language} - {submits}")
