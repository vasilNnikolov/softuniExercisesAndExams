n = int(input())

matrix = [list(map(int, input().split(" "))) for _ in range(n)]

command = input()

while command != "END":
    tokens = command.split(" ")
    r, c, value = map(int, tokens[1:])
    if not (0 <= r < n and 0 <= c < n):
        print("Invalid coordinates")
    else:
        if tokens[0] == "Add":
            matrix[r][c] += value
        elif tokens[0] == "Subtract":
            matrix[r][c] -= value

    command = input()

[print(" ".join(map(str, matrix[i]))) for i in range(n)]



