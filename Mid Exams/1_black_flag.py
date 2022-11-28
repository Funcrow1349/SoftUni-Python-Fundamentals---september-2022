days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range(1, days_of_plunder + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += daily_plunder * 0.50
    if day % 5 == 0:
        total_plunder -= total_plunder * 0.30

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:

    lacking_percentage = total_plunder * 100 / expected_plunder
    print(f"Collected only {lacking_percentage:.2f}% of the plunder.")