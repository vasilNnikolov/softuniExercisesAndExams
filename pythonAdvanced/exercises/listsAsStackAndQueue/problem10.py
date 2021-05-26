cups = input().split(" ")
cups = list(map(int, cups))

bottles = input().split(" ")
bottles = list(map(int, bottles))

wasted_water = 0

while len(bottles) > 0 and len(cups) > 0:
    water = bottles[-1]
    if water >= cups[0]:
        wasted_water += water - cups[0]
    cups[0] -= water
    if cups[0] <= 0:
        cups.pop(0)
    bottles.pop(-1)

if len(cups) == 0:
    print(f"Bottles: {' '.join(list(map(str, bottles[::-1])))}")

if len(bottles) == 0:
    print(f"Cups: {' '.join(list(map(str, cups)))}")

print(f"Wasted litters of water: {wasted_water}.")
