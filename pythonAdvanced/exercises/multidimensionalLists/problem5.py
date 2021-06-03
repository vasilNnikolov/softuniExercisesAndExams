size = tuple(map(int, input().split(" ")))

snake = input()
l = len(snake)

matrix = [["8" for i in range(size[1])] for j in range(size[0])]

def print_matrix(matrix):
    for i in range(len(matrix)):
        print("".join(list(map(str, matrix[i]))))

x, y, turn = 0, 0, 0
going_right = True
while turn < size[1]*size[0]:
    matrix[y][x] = snake[turn%l]
    if going_right:
        x += 1
    else:
        x -= 1
    turn += 1
    if x >= size[1] or x < 0:
        going_right = not going_right
        y += 1
        if x >= size[1]:
            x = size[1] - 1
        if x < 0:
            x = 0

print_matrix(matrix)




