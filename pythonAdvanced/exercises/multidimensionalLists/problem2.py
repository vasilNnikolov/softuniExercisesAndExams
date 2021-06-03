size = input().split(" ")
size = (int(size[0]), int(size[1]))

matrix = []

square_sidelength = 2

for _ in range(size[0]):
    matrix.append(input().split(" "))

count = 0
for y in range(size[0] - square_sidelength + 1):
    for x in range(size[1] - square_sidelength + 1):
        char = matrix[y][x]
        non_square = False
        for i in range(square_sidelength):
            for j in range(square_sidelength):
                if matrix[i + y][j + x] != char:
                    non_square = True
                    break
            if non_square:
                break
        if not non_square:
            count += 1

print(count)


