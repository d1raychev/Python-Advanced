from collections import deque
number_of_petrol_pumps = int(input())
tank = 0
pumps = deque()
start_position = 0
stops = 0
for _ in range(number_of_petrol_pumps):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

while stops < number_of_petrol_pumps:
    fuel = 0
    for i in range(number_of_petrol_pumps):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)

