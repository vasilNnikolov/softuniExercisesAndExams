
cards = input().split(':')

command = input()
deck = []
while command != 'Ready':
    tokens = command.split(' ')
    if tokens[0] == 'Add':
        name = tokens[1]
        if name in cards:
            deck.append(name)
        else:
            print('Card not found.')
    elif tokens[0] == 'Insert':
        name, index = tokens[1], int(tokens[2])
        if name not in cards or not (0 <= index < len(deck)):
            print('Error!')
        else:
            deck.insert(index, name)
    elif tokens[0] == 'Remove':
        name = tokens[1]
        if name in deck:
            deck.remove(name)
        else:
            print('Card not found.')
    elif tokens[0] == 'Swap':
        card1, card2 = tokens[1], tokens[2]
        i, j = 0, 0
        for k in range(len(deck)):
            if deck[k] == card1:
                i = k
            if deck[k] == card2:
                j = k
        deck[i] = card2
        deck[j] = card1

    elif tokens[0] == 'Shuffle':
        deck = deck[::-1]

    command = input()

print(' '.join(deck))