n = int(input())

pumps = []


for _ in range(n):
    command = input().split(" ")
    petrol, distance_to_next = int(command[0]), int(command[1])

    pumps.append((petrol, distance_to_next))

def check_pump(pumps, i):
    tank_capacity = 0
    for j in range(n):
        current_pump = (i + j) % n
        tank_capacity += pumps[current_pump][0] - pumps[current_pump][1]
        if tank_capacity < 0:
            return False
    return True

for pump_index in range(n):
    if check_pump(pumps, pump_index):
        print(pump_index)
        break
