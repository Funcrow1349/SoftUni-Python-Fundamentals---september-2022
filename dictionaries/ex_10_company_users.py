companies = {}
while True:
    command = input()
    if command == "End":
        break
    current_entry = command.split(" -> ")
    company = current_entry[0]
    employee_id = current_entry[1]
    if company not in companies.keys():
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company, employees in companies.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")