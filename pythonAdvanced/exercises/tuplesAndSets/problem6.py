n = int(input())

best_pair = []

for _ in range(n):
    command = input().split("-")
    first, second = command[0], command[1]
    first = first.split(",")
    second = second.split(",")
    first = list(map(int, first))
    second = list(map(int, second))

    intersection = min(first[1], second[1]) - max(first[0], second[0]) + 1
    if intersection > len(best_pair):
        longest_intersection = intersection
        best_pair = list(range(max(first[0], second[0]), 1 + min(first[1], second[1])))

print(f"Longest intersection is {best_pair} with length {len(best_pair)}")

