n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split(" "))))

sum_difference = 0

for i in range(n):
    sum_difference += (matrix[i][i] - matrix[i][n - i - 1])

print(abs(sum_difference))