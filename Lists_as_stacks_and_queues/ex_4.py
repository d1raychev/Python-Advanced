from collections import deque
water = int(input())

people = input()

water_list = deque()
while people != "Start":
    water_list.append(people)
    people = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_to_give = int(data[0])
        pearson_name = water_list.popleft()
        if liters_to_give <= water:
            print(f"{pearson_name} got water")
            water -= liters_to_give
        else:
            print(f"{pearson_name} must wait")
    else:
        liters_to_add = int(data[1])
        water += liters_to_add

    command = input()


print(f"{water} liters left")


