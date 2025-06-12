rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_rows = 0
max_cols = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_rows = row
            max_cols = col


print(f"Sum = {max_sum}")
max_substring = [matrix[r][max_cols:max_cols + 3] for r in range(max_rows, max_rows + 3)]
[print(*row) for row in max_substring]
