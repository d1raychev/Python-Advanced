numbers = [x for x in input().split()]
stack = []
while numbers:
    # print(numbers.pop(), end=" ")
    stack.append(numbers.pop())

print(" ".join(stack))
