size = input().split(" ")
size = (int(size[0]), int(size[1]))

matrix = []

for _ in range(size[0]):
    matrix.append(input().split(" "))

command = input()

def check_validity(command, size):
    tokens = command.split(" ")
    if len(tokens) != 5:
        return False
    if tokens[0] != "swap":
        return False
    if not (0 <= int(tokens[1]) < size[0]) or not (0 <= int(tokens[3]) < size[0]):
        return False
    if not (0 <= int(tokens[2]) < size[1]) or not (0 <= int(tokens[4]) < size[1]):
        return False
    return True

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(" ".join(list(map(str, matrix[i]))))

while command != "END":
    if check_validity(command, size):
        command = command.split(" ")
        y1, x1, y2, x2 = list(map(int, command[1:]))
        matrix[y1][x1], matrix[y2][x2] = matrix[y2][x2], matrix[y1][x1]
        print_matrix(matrix)
    else:
        print("Invalid input!")


    command = input()


