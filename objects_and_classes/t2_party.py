# creating the class
class Party:
    def __init__(self):
        self.people = []


# creating the object
party = Party()
while True:
    command = input()
    if command == "End":
        break
    # calling the method
    party.people.append(command)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
