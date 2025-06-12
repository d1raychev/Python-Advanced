stack = []
numbers = int(input())
for _ in range(numbers):
    qurey = input().split()
    if qurey[0] == "1":
        number = int(qurey[1])
        stack.append(number)
    elif stack:
        if qurey[0] == "2":
            stack.pop()
        elif qurey[0] == "3":
            print(max(stack))
        elif qurey[0] == "4":
            print(min(stack))

while stack:
    print(stack.pop(), end= "")
    if stack:
        print(", ", end= "")

# numbers = list(input().split())
