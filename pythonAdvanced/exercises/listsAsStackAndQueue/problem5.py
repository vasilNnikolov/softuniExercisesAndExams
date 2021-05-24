n = int(input())

distances = [0 for i in range(n)]  # distance from pump i to pump i + 1, or from (n-1) to 0
capacities = [0 for i in range(n)]

for i in range(n):
    capacity, distance = list(map(int, input().split(" ")))
    capacities[i] = capacity
    distances[i] = distance

solution_found = False


def get_best_solution(capacities, distances):
    for start_pump in range(n):
        truck_capacity = capacities[start_pump]
        for j in range(n + 1):
            current_pump = (j + start_pump) % n
            if truck_capacity > distances[current_pump]:
                # go to the next pump
                truck_capacity -= distances[current_pump]
                truck_capacity += capacities[current_pump]
                # check if this is the start pump
                if (current_pump + 1) % n == start_pump:
                    return start_pump
            else:
                break


forward = get_best_solution(capacities, distances)
reverse = get_best_solution(capacities[::-1], distances[::-1])
print(min(forward, n - reverse - 1))