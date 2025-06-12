green_light_duration = int(input())
free_window_duration = int(input())


cars_on_crossroad = []
crash = False
car_hit = ''
character_hit = ''
total_cars_passed = 0

while True:
    command = input()

    if command == "END":
        break

    elif command == "green":
        while cars_on_crossroad:
            car = cars_on_crossroad.pop(0)
            total_cars_passed += 1
            for i in range(green_light_duration):
                if not car:
                    break
                character = car[0]
                car = car[1:]
                if i == green_light_duration - 1 and car:
                    crash = True
                    car_hit = car
                    character_hit = character
                    break
            if crash:
                break

    else:
        cars_on_crossroad.append(command)

    if crash:
        break

if crash:
    print(f"A crash happened! {car_hit} was hit at {character_hit}.")
else:
    print(f"Everyone is safe. {total_cars_passed} total cars passed the crossroads.")