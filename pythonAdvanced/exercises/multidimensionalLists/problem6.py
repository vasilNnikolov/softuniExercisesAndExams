n = int(input())

board = []

for _ in range(n):
    board.append([c for c in input()])

number_of_attacks = {} # a dictionary with keys a tuple (row, col) of a knight, and values the number of knights it attacks

def get_number_of_attacks(y, x, board):
    total_attacks = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (abs(i) == 2 and abs(j) == 1) or (abs(i) == 1 and abs(j) == 2):
                if 0 <= y + i < len(board) and 0 <= x + j < len(board):
                    if board[y + i][x + j] == "K":
                        total_attacks += 1

    return total_attacks


for y in range(n):
    for x in range(n):
        if board[y][x] == "K":
            number_of_attacks[(y, x)] = get_number_of_attacks(y, x, board)

# sort the array
number_of_attacks = dict(sorted(number_of_attacks.items(), key=lambda entry: entry[1], reverse=True))

removed = 0
while sum(number_of_attacks.values()) > 0:
    first_key = number_of_attacks.keys()[0]
    board[first_key[0]][first_key[1]] = "0"
    removed += 1
    # recalculate dict
    number_of_attacks = {}  # a dictionary with keys a tuple (row, col) of a knight, and values the number of knights it attacks
    for y in range(n):
        for x in range(n):
            if board[y][x] == "K":
                number_of_attacks[(y, x)] = get_number_of_attacks(y, x, board)

    # sort the array
    number_of_attacks = dict(sorted(number_of_attacks.items(), key=lambda entry: entry[1], reverse=True))


print(removed)