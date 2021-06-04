categories = input().split(", ")

n = int(input())

inventory = {category: [] for category in categories} # value is a list of (item_name, quantity, quality)


for _ in range(n):
    command = input()
    category, item_name, data = command.split(" - ")
    data = data.split(";")
    quantity = int(data[0].split(":")[1])
    quality = int(data[1].split(":")[1])
    inventory[category].append((item_name, quantity, quality))

print(f"Count of items: {sum([sum([data[1] for data in inventory[category]]) for category in categories])}")

total_quality = sum([sum([data[2] for data in inventory[category]]) for category in categories])
print(f"Average quality: {total_quality/len(categories):.2f}")

[print(f"{category} ->", ", ".join([data[0] for data in inventory[category]])) for category in categories]


