from collections import deque

chocolate_array = list(map(int, input().split(", ")))
milk_array = list(map(int, input().split(", ")))

chocolate = deque(chocolate_array)
milk = deque(milk_array)

n_shakes = 5

while n_shakes > 0 and len(chocolate) > 0 and len(milk) > 0:
    if chocolate[-1] <= 0 or milk[0] <= 0:
        if chocolate[-1] <= 0:
            chocolate.pop()

        if milk[0] <= 0:
            milk.popleft()

        continue

    if len(chocolate) == 0 or len(milk) == 0:
        break


    if chocolate[-1] == milk[0]:
        n_shakes -= 1
        chocolate.pop()
        milk.popleft()
    else:
        chocolate[-1] -= 5

        first_milk = milk.popleft()
        milk.append(first_milk)


if n_shakes == 0:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolate) > 0:
    print(f"Chocolate: {', '.join(map(str, chocolate))}")
else:
    print("Chocolate: empty")

if len(milk) > 0:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")
