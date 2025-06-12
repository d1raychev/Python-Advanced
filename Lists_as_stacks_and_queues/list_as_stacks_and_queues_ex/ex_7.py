from collections import deque
robots_name = input().split(";")
robots = [(robot.split('-')[0], int(robot.split('-')[1])) for robot in robots_name]

hours, minutes, second = [int(x) for x in input().split(":")]
start_seconds =  hours * 3600 + minutes * 60 + second

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)
current_time = start_seconds
queue = deque(products)

while queue:
    product = queue.popleft()
    for robot_name, process_time in robots:
        busy_until = current_time + process_time
        if busy_until <= current_time:
            print(f"{robot_name} - {product} [{current_time//3600:02d}:{(current_time%3600)//60:02d}" f":{current_time%60:02d}]")
            current_time += 1
            break
    else:
        queue.append(product)
        current_time += 1
