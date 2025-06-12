text = tuple(input())

unice_sybwol = sorted(set(text))

for char in unice_sybwol:
    print(f"{char}: {text.count(char)} time/s")