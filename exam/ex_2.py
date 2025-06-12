import sys

text = sys.stdin.read

# Read input
data = input().strip().split('\n')
n = int(data[0])
matrix = [list(data[i + 1]) for i in range(n)]
commands = data[n + 1:]

# Find initial positions of 'B' and 'H'
bee_position = None
hive_position = None

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'B':
            bee_position = (i, j)
        elif matrix[i][j] == 'H':
            hive_position = (i, j)

# Initialize bee's initial conditions
energy = 15
collected_nectar = 0
successful = False

# Execute commands
for command in commands:
    if energy <= 0:
        break

    # Move the bee according to the command
    current_row, current_col = bee_position
    if command == 'up':
        current_row -= 1
    elif command == 'down':
        current_row += 1
    elif command == 'left':
        current_col -= 1
    elif command == 'right':
        current_col += 1

    # Handle boundaries (wrap around)
    if current_row < 0:
        current_row = n - 1
    elif current_row >= n:
        current_row = 0
    if current_col < 0:
        current_col = n - 1
    elif current_col >= n:
        current_col = 0

    # Update bee's position
    if matrix[current_row][current_col].isdigit():
        nectar = int(matrix[current_row][current_col])
        collected_nectar += nectar
        matrix[current_row][current_col] = '-'
        energy -= 1
    elif matrix[current_row][current_col] == '-':
        energy -= 1
    elif matrix[current_row][current_col] == 'H':
        successful = True
        break

    bee_position = (current_row, current_col)
    energy -= 1

# Determine final outcome based on collected nectar and energy
if successful:
    if collected_nectar >= 30:
        if energy <= 0:
            print(f"Great job, Beesy! The hive is full. Energy left: 0")
        else:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
    else:
        print("Beesy did not manage to collect enough nectar.")
else:
    if collected_nectar >= 30:
        print(f"This is the end! Beesy ran out of energy.")
    else:
        print(f"This is the end! Beesy ran out of energy.")

# Print final state of the matrix
for row in matrix:
    print(''.join(row))
