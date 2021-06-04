r, c = map(int, input().split(" "))

a = "a"
matrix = [[f"{chr(ord(a) + y)}{chr(ord(a) + x + y)}{chr(ord(a) + y)}" for x in range(c)] for y in range(r)]

[print(" ".join(matrix[y][x] for x in range(c))) for y in range(r)]