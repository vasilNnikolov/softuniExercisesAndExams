n = int(input())
cars = {}


for _ in range(n):
    car, mileage, fuel = input().split('|')
    mileage, fuel = int(mileage), int(fuel)
    cars[car] = [mileage, fuel]

gas_tank_capacity = 75
command = input()
while command != 'Stop':
    tokens = command.split(' : ')
    if tokens[0] == 'Drive':
        car, distance, fuel = tokens[1], int(tokens[2]), int(tokens[3])
        if car in cars:
            if fuel > cars[car][1]:
                print('Not enough fuel to make that ride')
            else:
                cars[car][1] -= fuel
                cars[car][0] += distance
                print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
                if cars[car][0] >= 100000:
                    print(f'Time to sell the {car}!')
                    cars.pop(car)

    elif tokens[0] == 'Refuel':
        car, added_fuel = tokens[1], int(tokens[2])
        if car in cars:
            if added_fuel + cars[car][1] > gas_tank_capacity:
                added_fuel = gas_tank_capacity - cars[car][1]
            print(f'{car} refueled with {added_fuel} liters')

    elif tokens[0] == 'Revert':
        car, km = tokens[1], int(tokens[2])
        if car in cars:
            if cars[car][0] - km > 10000:
                cars[car][0] -= km
                print(f'{car} mileage decreased by {km} kilometers')
            else:
                cars[car][0] = 10000

    command = input()


cars = dict(sorted(cars.items(), key=lambda x: x[0]))

cars = dict(sorted(cars.items(), key=lambda x: x[1][0], reverse=True))

for car in cars:
    print(f'{car} -> Mileage: {cars[car][0]:.0f} kms, Fuel in the tank: {cars[car][0]:.0f} lt.')
