n = int(input())

elements = set()

for _ in range(n):
    entries = set(input().split(" "))
    elements |= entries

for e in elements:
    print(e)
