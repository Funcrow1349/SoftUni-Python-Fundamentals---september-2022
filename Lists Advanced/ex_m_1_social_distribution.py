def wealth_distributor(people, wealth):
    if sum(people) / len(people) < wealth:
        return "No equal distribution possible"
    else:
        for index in range(len(people)):
            if people[index] < wealth:
                difference = wealth - people[index]
                people[index] += difference
                index_of_richest_person = people.index(max(people))
                people[index_of_richest_person] -= difference
        return people


population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())
print(wealth_distributor(population, minimum_wealth))