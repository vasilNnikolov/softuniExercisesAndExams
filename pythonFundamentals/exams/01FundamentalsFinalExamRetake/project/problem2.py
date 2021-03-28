import re

text = input()

hash_regex = r"#([a-zA-Z\s]{1,})#(\d{2}/\d{2}/\d{2})#(\d{1,})#"
pipe_regex = r"\|([a-zA-Z\s]{1,})\|(\d{2}/\d{2}/\d{2})\|(\d{1,})\|"

matches = re.finditer(hash_regex, text)
foods = {}
for match in matches:
    foods[match.start()] = match.groups()

matches = re.finditer(pipe_regex, text)
for match in matches:
    foods[match.start()] = match.groups()

foods = dict(sorted(foods.items(), key=lambda food: food[0]))
calories = sum([int(food[2]) for food in foods.values()])

days = calories // 2000

print(f"You have food to last you for: {days} days!")

for food in foods.values():
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")

