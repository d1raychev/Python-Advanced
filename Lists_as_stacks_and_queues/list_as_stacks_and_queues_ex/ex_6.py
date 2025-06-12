from collections import deque

expression = deque(input())
start_index = "([{"
end_index = ")]}"
counter = 0
while expression and counter < len(expression) / 2:
    if expression[0] not in start_index:
        break
    index = start_index.index(expression[0])
    if expression[1] == end_index[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(counter)
        counter = 0
    else:
        counter += 1
        expression.rotate(-1)
if expression:
    print("NO")
else:
    print("YES")

