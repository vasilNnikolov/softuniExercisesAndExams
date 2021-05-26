
green_time = int(input())
free_time = int(input())

def char_in_middle(cars, green_time, free_time, pointer, total_cars):
    total_cars += cars[pointer: pointer + min(green_time, len(cars) - pointer - 1)].count("%")
    pointer += min(green_time, len(cars) - pointer - 1)
    for t in range(free_time):
        if cars[pointer] == "%":
            total_cars += 1
            break
        pointer += 1

    return pointer, total_cars



command = input()
horizontal = [] # and array of the characters of the cars, separated by %
vertical = [] # and array of the characters of the cars, separated by %
horizontal_pointer, vertical_pointer = 0, 0
is_horizontal = True
total_cars = 0
while command != "END":
    while command != "green":
        if is_horizontal:
            horizontal.extend([c for c in command])
            horizontal.append("%")
        else:
            vertical.extend([c for c in command])
            vertical.append("%")

        command = input()
    middle_char = "%"
    pointer = 0
    if is_horizontal:
        pointer, total_cars = char_in_middle(horizontal, green_time, free_time, horizontal_pointer, total_cars)
        middle_char = horizontal[pointer]
    else:
        pointer, total_cars = char_in_middle(vertical, green_time, free_time, vertical_pointer, total_cars)
        middle_char = vertical[pointer]

    if middle_char != "%": # a non-empty char in the middle of the crossroads after the end of the free time
        print("A crash happened!")

        # determine the car which caused the crash
        car_beginning, car_end = pointer, pointer
        if is_horizontal:
            while horizontal[car_beginning] != "%":
                car_beginning -= 1
            while horizontal[car_end] != "%":
                car_end += 1
            car = horizontal[car_beginning + 1: car_end]
            car = "".join(car)
            print(f"{car} was hit at {horizontal[pointer + 1]}.")
        else:
            while vertical[car_beginning] != "%":
                car_beginning -= 1
            while vertical[car_end] != "%":
                car_end += 1
            car = vertical[car_beginning + 1: car_end]
            car = "".join(car)
            print(f"{car} was hit at {vertical[pointer + 1]}.")

        break

    is_horizontal = not is_horizontal
    command = input()

if command == "END": # no crash
    print("Everyone is safe.")
    print(f"{total_cars} total cars passed the crossroads.")





