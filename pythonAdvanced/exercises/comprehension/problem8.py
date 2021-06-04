heroes = input().split(", ")

command = input()
inventories = {hero: [] for hero in heroes} # key is hero name, value is list of tuples (item, cost)

while command != "End":
    hero, item, cost = command.split("-")
    cost = int(cost)
    if item not in [item[0] for item in inventories[hero]]:
        inventories[hero].append((item, cost))

    command = input()

for hero in inventories:
    print(f"{hero} -> Items: {len(inventories[hero])}, Cost: {sum([item[1] for item in inventories[hero]])}")