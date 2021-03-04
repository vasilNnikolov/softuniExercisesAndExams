inventory = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
legendaryItems = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
obtained = False
while True:
    items = input().split(' ')
    for i in range(1, len(items), 2):
        item, quantity = items[i].lower(), int(items[i - 1])
        if not obtained:
            if item in inventory.keys():
                inventory[item] += quantity
                if inventory[item] >= 250:
                    print(f'{legendaryItems[item]} obtained!')
                    inventory[item] -= 250
                    inventory = dict(sorted(inventory.items(), key=lambda x: x[0]))
                    inventory = dict(sorted(inventory.items(), key=lambda x: x[1], reverse=True))
                    for inventoryItem, inventoryQuantity in inventory.items():
                        print(f'{inventoryItem}: {inventoryQuantity}')
                    junk = dict(sorted(junk.items(), key=lambda x: x[0]))
                    for junkItem, junkQuantity in junk.items():
                        print(f'{junkItem}: {junkQuantity}')
                    obtained = True

            elif item in junk.keys():
                junk[item] += quantity
            else:
                junk[item] = quantity
    if obtained:
        break