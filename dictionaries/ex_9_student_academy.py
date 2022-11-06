grades = {}
pair_of_rows = int(input())
for row in range(pair_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in grades.keys():
        grades[student_name] = []
    grades[student_name].append(grade)
for student, grade in grades.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")


