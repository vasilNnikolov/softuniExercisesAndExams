companies = {}

command = input()

while command != 'End':
    name, personId = command.split(' -> ')

    if name not in companies:
        companies[name] = [personId]
    else:
        if personId not in companies[name]:
            companies[name].append(personId)

    command = input()

companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for name in companies.keys():
    print(name)
    for id in companies[name]:
        print(f'-- {id}')