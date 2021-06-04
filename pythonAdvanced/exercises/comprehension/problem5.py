n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split(", "))))
diagonal1 = [matrix[i][i] for i in range(n)]
diagonal2 = [matrix[i][n - i - 1] for i in range(n)]

print(f"First diagonal: {', '.join(list(map(str, diagonal1)))}. Sum: {sum(diagonal1)}")
print(f"Second diagonal: {', '.join(list(map(str, diagonal2)))}. Sum: {sum(diagonal2)}")
