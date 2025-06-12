numbers = tuple(float(el) for el in input().split())

occ = {}
for n in numbers:
    if n not in occ:
        occ[n] = numbers.count(n)
        print(f"{n} - {numbers.count(n)} times")

