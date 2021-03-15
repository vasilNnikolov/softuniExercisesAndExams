text = input()
text = list(text)
N = int(input())

field = [[] for _ in range(N)]
x, y = 0, 0  # player x and y coordinates
for line_index in range(N):
    line = input()
    letters = list(line)
    if "P" in letters:
        y = line_index
        x = letters.index("P")

    field[line_index] = letters

M = int(input())

for _ in range(M):
    command = input()

    if command == "up":
        if y > 0:
            field[y][x] = "-"
            y -= 1
            if field[y][x] != "-":
                text.append(field[y][x])
                field[y][x] = "-"

        else:
            # punish player
            if len(text) > 0:
                text.pop(-1)

    if command == "down":
        if y < N - 1:
            field[y][x] = "-"
            y += 1
            if field[y][x] != "-":
                text.append(field[y][x])
                field[y][x] = "-"

        else:
            # punish player
            if len(text) > 0:
                text.pop(-1)

    if command == "left":
        if x > 0:
            field[y][x] = "-"
            x -= 1
            if field[y][x] != "-":
                text.append(field[y][x])
                field[y][x] = "-"

        else:
            # punish player
            if len(text) > 0:
                text.pop(-1)

    if command == "right":
        if x < N - 1:
            field[y][x] = "-"
            x += 1
            if field[y][x] != "-":
                text.append(field[y][x])
                field[y][x] = "-"

        else:
            # punish player
            if len(text) > 0:
                text.pop(-1)
field[y][x] = "P"
print("".join(text))
for y in range(N):
    print("".join(field[y]))
