data = int(input())


matrix = []
for rows in range(data):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

sum_of = 0

for rows_index in range(data):
    sum_of += matrix[rows_index][rows_index]
print(sum_of)

