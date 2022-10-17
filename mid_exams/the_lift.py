nr_of_people = int(input())
wagons_seats = [int(num) for num in input().split()]
empty_seats = 0

for index in range(len(wagons_seats)):
    if wagons_seats[index] < 4:
        empty_seats += 4 - wagons_seats[index]
        if nr_of_people >= empty_seats:
            wagons_seats[index] += empty_seats
            nr_of_people -= empty_seats
            empty_seats = 0
        elif nr_of_people < empty_seats:
            empty_seats -= nr_of_people
            wagons_seats[index] += nr_of_people
            nr_of_people = 0


wagons_seats = " ".join([str(num) for num in wagons_seats])
if nr_of_people == 0 and empty_seats > 0:
    print("The lift has empty spots!")
    print(wagons_seats)
elif nr_of_people > 0 and empty_seats == 0:
    print(f"There isn't enough space! {nr_of_people} people in a queue!")
    print(wagons_seats)
elif nr_of_people == 0 and empty_seats == 0:
    print(wagons_seats)

