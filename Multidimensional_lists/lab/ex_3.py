rows = int(input())

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

flatted = []

for row_index in range(rows):
    for cool_index in range(len(matrix[row_index])):
        flatted.append(matrix[row_index][cool_index])

print(flatted)