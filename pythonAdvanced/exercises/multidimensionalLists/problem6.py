attackable_positions = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]

n = int(input())

board = []

def is_on_board(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

for _ in range(n):
    board.append([c for c in input()])

attacking = {} # key is (row, col) of knight, value is a list of all coordinates which it attacks and there are knights
for y in range(n):
    for x in range(n):
        if board[y][x] == "K":
            attacking[(y, x)] = []


for y in range(n):
    for x in range(n):
        if board[y][x] == "K":
            for p in attackable_positions:
                x1, y1 = x + p[0], y + p[1]
                if is_on_board(x1, y1):
                    if board[y1][x1] == "K":
                        attacking[(y, x)].append((y1, x1))

removed_knights = 0
while sum([len(i) for i in attacking.values()]) != 0:
    # get key which attacks the highest number of other knights
    most_angry_knight = max(attacking.items(), key=lambda item: len(item[1]))
    attacking.pop(most_angry_knight[0])
    for knight in attacking:
        if most_angry_knight[0] in attacking[knight]:
            attacking[knight].remove(most_angry_knight[0])

    removed_knights += 1


print(removed_knights)




