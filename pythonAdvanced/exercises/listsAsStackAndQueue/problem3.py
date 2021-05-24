from collections import deque

total_food = int(input())

orders = input().split(" ")

orders = deque(list(map(int, orders)))

print(max(orders))
while len(orders) > 0 and total_food >= orders[0]:
    total_food -= orders[0]
    orders.popleft()

if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(i) for i in list(orders)])}")


