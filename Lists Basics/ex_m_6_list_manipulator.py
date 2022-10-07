import sys

initial_entry = input().split()
line_of_integers = []
for string in initial_entry:
    line_of_integers.append(int(string))
current_command = input()

while current_command != "end":
    if "exchange" in current_command:
        current_command = current_command.split()
        index_ex = int(current_command[1])
        mutated_list = []
        if int(current_command[1]) < 0 or int(current_command[1]) >= len(line_of_integers):
            print("Invalid index")
        else:
            for a in range(index_ex + 1, len(line_of_integers)):
                mutated_list.append(line_of_integers[a])
            for b in range(0, index_ex + 1):
                mutated_list.append(line_of_integers[b])
        line_of_integers = mutated_list
    elif "max" in current_command:
        no_matches = True
        if "odd" in current_command:
            max_odd_index = 0
            max_odd_number = -sys.maxsize
            for c in range(len(line_of_integers)):
                if line_of_integers[c] % 2 != 0 and line_of_integers[c] >= max_odd_number:
                    max_odd_index = c
                    max_odd_number = line_of_integers[c]
                    no_matches = False
                else:
                    continue
            if not no_matches:
                print(max_odd_index)
        elif "even" in current_command:
            max_even_index = 0
            max_even_number = -sys.maxsize
            for d in range(len(line_of_integers)):
                if line_of_integers[d] % 2 == 0 and line_of_integers[d] >= max_even_number:
                    max_even_index = d
                    max_even_number = line_of_integers[d]
                    no_matches = False
                else:
                    continue
            if not no_matches:
                print(max_even_index)
        if no_matches:
            print("No matches")
    elif "min" in current_command:
        no_matches = True
        if "odd" in current_command:
            min_odd_index = 0
            min_odd_number = sys.maxsize
            for e in range(len(line_of_integers)):
                if line_of_integers[e] % 2 != 0 and line_of_integers[e] <= min_odd_number:
                    min_odd_index = e
                    min_odd_number = line_of_integers[e]
                    no_matches = False
                else:
                    continue
            if not no_matches:
                print(min_odd_index)
        elif "even" in current_command:
            min_even_index = 0
            min_even_number = sys.maxsize
            for f in range(len(line_of_integers)):
                if line_of_integers[f] % 2 == 0 and line_of_integers[f] <= min_even_number:
                    min_even_index = f
                    min_even_number = line_of_integers[f]
                    no_matches = False
                else:
                    continue
            if not no_matches:
                print(min_even_index)
        if no_matches:
            print("No matches")
    elif "first" in current_command:
        first_list = []
        if "even" in current_command:
            current_command = list(current_command)
            index_first = 0
            while len(first_list) < int(current_command[6]):
                if index_first > len(line_of_integers):
                    break
                if int(current_command[6]) > len(line_of_integers):
                    break
                if line_of_integers[index_first] % 2 == 0:
                    first_list.append(line_of_integers[index_first])
                index_first += 1
        elif "odd" in current_command:
            current_command = list(current_command)
            index_second = 0
            while len(first_list) < int(current_command[6]):
                if index_second > len(line_of_integers):
                    break
                if int(current_command[6]) > len(line_of_integers):
                    break
                if line_of_integers[index_second] % 2 != 0:
                    first_list.append(line_of_integers[index_second])
                index_second += 1
        if int(current_command[6]) > len(line_of_integers):
            print("Invalid count")
        else:
            print(first_list)
    elif "last" in current_command:
        last_list = []
        if "even" in current_command:
            current_command = list(current_command)
            index_last = len(line_of_integers) - 1
            while len(last_list) < int(current_command[5]):
                if index_last < 0:
                    break
                if int(current_command[5]) > len(line_of_integers):
                    break
                if line_of_integers[index_last] % 2 == 0:
                    last_list.append(line_of_integers[index_last])
                index_last -= 1
        elif "odd" in current_command:
            current_command = list(current_command)
            index_mid = len(line_of_integers) - 1
            while len(last_list) < int(current_command[5]):
                if index_mid < 0:
                    break
                if int(current_command[5]) > len(line_of_integers):
                    break
                if line_of_integers[index_mid] % 2 != 0:
                    last_list.append(line_of_integers[index_mid])
                index_mid -= 1
        if int(current_command[5]) > len(line_of_integers):
            print("Invalid count")
        else:
            print(last_list)
    current_command = input()
print(line_of_integers)
