data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []
for rows_index in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for col_index in range(cols):
    sum_of = 0
    for rows_index in range(rows):
        sum_of += matrix[rows_index][col_index]
    print(sum_of)