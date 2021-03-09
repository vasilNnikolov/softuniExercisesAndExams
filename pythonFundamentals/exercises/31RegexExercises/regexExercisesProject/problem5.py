import re

pattern = r'>>(\w+)<<(\d+(\.\d+)*)!(\d+)'

command = input()
total_cost = 0
items_bought = []
while command != 'Purchase':
    m = re.match(pattern, command)
    if m:
        tokens = m.groups()
        item, price, quantity = tokens[0], float(tokens[1]), int(tokens[3])
        total_cost += price*quantity
        items_bought.append(item)
    command = input()

print('Bought furniture:')
for item in items_bought:
    print(item)
print(f'Total money spend: {total_cost:.2f}')