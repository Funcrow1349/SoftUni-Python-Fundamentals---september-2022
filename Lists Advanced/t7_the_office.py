employees = input().split()
happiness_improvement_factor = int(input())
employees = list(map(lambda emp: int(emp) * happiness_improvement_factor, employees))
filtered = list(filter(lambda emp: emp >= (sum(employees) / len(employees)), employees))
if len(filtered) >= len(employees) // 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")
