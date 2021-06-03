size = input().split(" ")
size = (int(size[0]), int(size[1]))

matrix = []

square_sidelength = 3

for _ in range(size[0]):
    matrix.append(list(map(int, input().split(" "))))

best_sum = 0
best_square = [[0 for _ in range(square_sidelength)] for j in range(square_sidelength)]
for y in range(size[0] - square_sidelength + 1):
    for x in range(size[1] - square_sidelength + 1):
        sum = 0
        for i in range(square_sidelength):
            for j in range(square_sidelength):
                sum += matrix[y + i][x + j]

        if sum > best_sum:
            best_sum = sum
            best_square = [matrix[y + i][x:x + square_sidelength] for i in range(square_sidelength)]


print(f"Sum = {best_sum}")

for i in range(square_sidelength):
    print(" ".join(list(map(str, best_square[i]))))



