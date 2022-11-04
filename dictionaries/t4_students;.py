command = input().split(":")
students = {}

while len(command) > 1:
    name, ident, course = command[0], command[1], command[2]
    if course not in students:
        students[course] = []
    students[course].append(f"{name} - {ident}")
    command = input().split(":")

searched_element = command[0].replace("_", " ")
for student in students[searched_element]:
    print(student)
