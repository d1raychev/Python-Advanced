numbers_line_1 = set(int(x) for x in input().split())
numbers_line_2 = set(int(x) for x in input().split())

count_numbers = int(input())

for n in range(count_numbers):
    line = input().split()
    command = line[0] + " " + line[1]
    digits = [int(num) for num in line[2:]]
    if command == "Add First":
        numbers_line_1.update(digits)
    elif command == "Add Second":
        numbers_line_2.update(digits)
    elif command == "Remove First":
        numbers_line_1.difference_update(digits)
    elif command == "Remove Second":
        numbers_line_2.difference_update(digits)
    elif command == "Check Subset":
        print(numbers_line_1.issubset(numbers_line_2)
              or numbers_line_2.issubset(numbers_line_1))

print(*sorted(numbers_line_1), sep=", ")
print(*sorted(numbers_line_2), sep=", ")
