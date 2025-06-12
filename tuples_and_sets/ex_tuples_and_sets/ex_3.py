numbers = int(input())
n = set()
for _ in range(numbers):
    elements = input().split()
    for el in elements:
        n.add(el)

print("\n".join(n))