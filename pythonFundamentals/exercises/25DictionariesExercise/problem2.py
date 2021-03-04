resourses = {}

command = input()

while command != 'stop':
    material = command
    quantity = int(input())
    if material in resourses.keys():
        resourses[material] += quantity
    else:
        resourses[material] = quantity
    command = input()
for key, value in resourses.items():
    print(f'{key} -> {value}')