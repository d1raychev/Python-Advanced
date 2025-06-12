numbers = int(input())
container = set()
for n in range(numbers):
    names = input()
    container.add(names)
print("\n".join(container))