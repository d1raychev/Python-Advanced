from collections import deque

materials = [int(num) for num in input().split()]
magic = deque(int(x) for x in input().split())

points = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
present = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in points:
        new_present = points[total_magic]
        if new_present not in present:
            present[new_present] = 0
        present[new_present] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic == 0:
        materials.pop()
        magic.popleft()
    elif magic[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()

if ("Doll" in present and "Wooden train" in present) or ("Teddy bear" in present and "Bicycle" in present):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(present.items()):
    if value > 0:
        print(f"{key}: {value}")
