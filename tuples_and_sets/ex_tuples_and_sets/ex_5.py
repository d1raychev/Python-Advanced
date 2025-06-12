number = int(input())

longest_interseption = set()

for n in range(number):
    fist_range, second_range = input().split("-")
    first_start, first_end = [int(x) for x in fist_range.split(",")]
    second_start, second_end = [int(x) for x in second_range.split(",")]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    interseption = first_set & second_set

    if len(interseption) > len(longest_interseption):
        longest_interseption = interseption

print(f"Longest intersection is {list(longest_interseption)} with length {len(longest_interseption)}")
