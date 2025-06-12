clothes_stack = [int(x) for x in input().split()]
capacity_counter = 0
capacity_of_rack = int(input())
while clothes_stack:
    capacity_counter += 1
    current_capacity = capacity_of_rack
    while clothes_stack and clothes_stack[-1] <= current_capacity:
        current_capacity -= clothes_stack.pop()

print(capacity_counter)
