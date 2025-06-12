data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []
sum_nums = 0

for _ in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)
    sum_nums += sum(elements)


print(sum_nums)
print(matrix)
