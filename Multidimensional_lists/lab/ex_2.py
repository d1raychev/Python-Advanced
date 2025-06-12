rows = int(input())

matrix = []

for row_index in range(rows):
    elements = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(elements)


print(matrix)
# even_matrix = []

# for row_index in range(rows):
#     even_matrix.append([])
#     for cool_index in range(len(matrix[row_index])):
#         curent_element = matrix[row_index][cool_index]
#         if curent_element % 2 == 0:
#             even_matrix[row_index].append(curent_element)
#
# print(even_matrix)
