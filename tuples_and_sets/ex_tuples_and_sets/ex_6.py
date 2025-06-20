numbers = int(input())

odd_set = set()
even_set = set()
for n in range(1, numbers + 1):
    name_sum = sum([ord(char) for char in input()]) // n
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=", ")

