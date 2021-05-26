command = input().split(" ")
n, m = int(command[0]), int(command[1])

first, second = set(), set()

for _ in range(n):
    first.add(int(input()))

for _ in range(m):
    second.add(int(input()))

result = set(first)

for c in first:
    if c not in second:
        result.remove(c)

for c in result:
    print(c)
