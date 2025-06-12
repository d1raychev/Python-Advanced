from collections import deque

numbers_of_orders = int(input())

orders_queue = deque([int(x) for x in input().split()])
print(max(orders_queue))
while orders_queue and orders_queue[0] < numbers_of_orders:
    numbers = orders_queue[0]
    numbers_of_orders -= numbers
    orders_queue.popleft()

if orders_queue:
    print('Orders left:', end="")
    while orders_queue:
        print(f' {orders_queue.popleft()}', end="")
else:
    print("Orders complete")




