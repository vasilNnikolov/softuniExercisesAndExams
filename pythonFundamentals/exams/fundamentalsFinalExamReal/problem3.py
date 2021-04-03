
command = input()
people = {} # key is person name, value is a list of [health, energy]

while command != "Results":
    tokens = command.split(":")
    if tokens[0] == "Add":
        person_name, health, energy = tokens[1], int(tokens[2]), int(tokens[3])
        if person_name not in people:
            people[person_name] = [health, energy]
        else:
            people[person_name][0] += health

    elif tokens[0] == "Attack":
        attacker_name, defender_name, damage = tokens[1], tokens[2], int(tokens[3])
        if attacker_name in people and defender_name in people:
            people[defender_name][0] -= damage
            people[attacker_name][1] -= 1
            if people[defender_name][0] <= 0:
                print(f"{defender_name} was disqualified!")
                del people[defender_name]
            if people[attacker_name][1] <= 0:
                print(f"{attacker_name} was disqualified!")
                del people[attacker_name]

    elif tokens[0] == "Delete":
        if tokens[1] == "All":
            people = {}
        else:
            if tokens[1] in people:
                del people[tokens[1]]

    command = input()

people = dict(sorted(people.items(), key=lambda item: item[0]))
people = dict(sorted(people.items(), key=lambda item: item[1][0], reverse=True))

print(f"People count: {len(people)}")
for name in people:
    print(f"{name} - {people[name][0]} - {people[name][1]}")

