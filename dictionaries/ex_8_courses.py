courses = {}
while True:
    command = input()
    if command == "end":
        break
    current_input = command.split(" : ")
    course_name = current_input[0]
    student_name = current_input[1]
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)

for course, student_names in courses.items():
    print(f"{course}: {len(student_names)}")
    for student in student_names:
        print(f"-- {student}")
