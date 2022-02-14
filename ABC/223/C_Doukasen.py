n = int(input())

total = 0
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    total += a / b
    ab.append((a, b))

half = total / 2

dist = 0
for a, b in ab:
    sp = a / b
    if half > sp:
        half -= sp
        dist += a
    else:
        dist += half * b
        print(dist)
        exit()