sides = {} # key is side name, value is list of users on that side

command = input()
def isUnique(user, sides: dict):
    allUsers = []
    [allUsers.extend(sideUsers) for sideUsers in sides.values()]
    return not user in allUsers

while command != 'Lumpawaroo':
    if command.__contains__('|'):
        tokens = command.split(' | ')
        side, user = tokens[0], tokens[1]
        if isUnique(user, sides):
            if side not in sides:
                sides[side] = [user]
            else:
                if user not in sides[side]:
                    sides[side].append(user)

    elif command.__contains__('->'):
        tokens = command.split(' -> ')
        newSide, user = tokens[1], tokens[0]
        userExists = False
        for s, users in sides.items():
            if user in users:
                sides[s].remove(user)
                if newSide not in sides:
                    sides[newSide] = [user]
                else:
                    if user not in sides[newSide]:
                        sides[newSide].append(user)
                userExists = True
                break
        if not userExists:
            if newSide not in sides:
                sides[newSide] = [user]
            else:
                if user not in sides[newSide]:
                    sides[newSide].append(user)
        print(f'{user} joins the {newSide} side!')
    command = input()

sides = dict(sorted(sides.items(), key=lambda x: x[0]))
sides = dict(sorted(sides.items(), key=lambda x: len(x[1]), reverse=True))

for sideName, sideUsers in sides.items():
    if len(sideUsers) > 0:
        print(f'Side: {sideName}, Members: {len(sideUsers)}')
        sideUsers.sort()
        for u in sideUsers:
            print(f'! {u}')