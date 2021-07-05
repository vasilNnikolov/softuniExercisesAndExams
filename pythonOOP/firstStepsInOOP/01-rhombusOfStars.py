def print_line(n, row):
    for _ in range(n - row - 1):
        print(" ", end="")
    for _ in range(row + 1):
        print("*", end=" ")
    print()


n = int(input())
for i in range(n):
    print_line(n, i)
for i in range(n):
    print_line(n, n - i - 2)