clothes = input().split(" ")

clothes = list(map(int, clothes))

rack_capacity = int(input())

n_racks = 1

rack_fill = 0
while len(clothes) > 0:
    if rack_fill + clothes[0] <= rack_capacity:
        rack_fill += clothes[0]
        clothes.pop(0)
    else:
        n_racks += 1
        rack_fill = 0

print(n_racks)


