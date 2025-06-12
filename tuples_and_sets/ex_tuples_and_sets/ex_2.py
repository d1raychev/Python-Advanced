n,m = [int(x) for x in input().split()]

set_1 = set()
set_2 = set()
for _ in range(n):
    set_1.add(input())
for _ in range(m):
    set_2.add(input())

print("\n".join(set_1 & set_2))