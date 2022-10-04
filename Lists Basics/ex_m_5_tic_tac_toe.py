first_line = input().split()
second_line = input().split()
third_line = input().split()
nr_of_zeroes = 0
nr_of_ones = 0
nr_of_twos = 0

for nr in range(len(first_line)):
    if first_line[nr] == "1":
        nr_of_ones += 1
    elif first_line[nr] == "2":
        nr_of_twos += 1
    else:
        nr_of_zeroes += 1
for nr in range(len(second_line)):
    if second_line[nr] == "1":
        nr_of_ones += 1
    elif second_line[nr] == "2":
        nr_of_twos += 1
    else:
        nr_of_zeroes += 1
for nr in range(len(third_line)):
    if third_line[nr] == "1":
        nr_of_ones += 1
    elif third_line[nr] == "2":
        nr_of_twos += 1
    else:
        nr_of_zeroes += 1

if nr_of_ones >= 3 or nr_of_twos >= 3:
    if nr_of_ones > nr_of_twos:
        print("First player won")
    elif nr_of_twos > nr_of_ones:
        print("Second player won")
    else:
        print("Draw!")


