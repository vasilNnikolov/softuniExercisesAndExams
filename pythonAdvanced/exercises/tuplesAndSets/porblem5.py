
phonebook = {}

command = input()

while not command.isdigit():
    tokens = command.split("-")
    name, number = tokens[0], tokens[1]
    phonebook[name] = number
    command = input()

n = int(command)

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

