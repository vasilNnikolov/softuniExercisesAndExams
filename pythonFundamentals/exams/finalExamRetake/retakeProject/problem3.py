
class Car:
    def __init__(self, name: str, mileage: int, fuel: int):
        self.name = name
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, distance, fuel_used):
        if self.fuel < fuel_used:
            print("Not enough fuel to make that ride")
        else:
            self.fuel -= fuel_used
            self.mileage += distance
            print(f"{self.name} driven for {distance} kilometers. {fuel_used} liters of fuel consumed.")
            if self.mileage > max_mileage:
                print(f"Time to sell the {self.name}!")

    def refuel(self, added_fuel):
        added_fuel = int(added_fuel)
        if self.fuel + added_fuel > tank_capacity:
            added_fuel = tank_capacity - self.fuel

        self.fuel += added_fuel
        print(f"{self.name} refueled with {added_fuel} liters")

    def revert(self, kilometers):
        if self.mileage - kilometers < min_mileage:
            self.mileage = min_mileage
        else:
            self.mileage -= kilometers
            print(f"{self.name} mileage decreased by {kilometers} kilometers")


n = int(input())
cars = {} # key is car name, value is Car object

tank_capacity = 75
max_mileage = 100000
min_mileage = 10000

for _ in range(n):
    car, mileage, fuel = input().split('|')
    mileage, fuel = int(mileage), int(fuel)
    cars[car] = Car(car, mileage, fuel)

command = input()
while command != 'Stop':
    tokens = command.split(' : ')
    if tokens[0] == 'Drive':
        car, distance, fuel = tokens[1], int(tokens[2]), int(tokens[3])
        if car in cars:
            cars[car].drive(distance, fuel)
            if cars[car].mileage > max_mileage:
                cars.pop(car)

    elif tokens[0] == 'Refuel':
        car, added_fuel = tokens[1], int(tokens[2])
        if car in cars:
            cars[car].refuel(added_fuel)

    elif tokens[0] == 'Revert':
        car, km = tokens[1], int(tokens[2])
        if car in cars:
            cars[car].revert(km)

    command = input()


cars = dict(sorted(cars.items(), key=lambda car: car[1].name))

cars = dict(sorted(cars.items(), key=lambda car: car[1].mileage, reverse=True))
for car in cars.values():
    print(f'{car.name} -> Mileage: {car.mileage} kms, Fuel in the tank: {car.fuel} lt.')
