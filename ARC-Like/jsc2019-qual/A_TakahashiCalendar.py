m, d = map(int, input().split())

day = 0
for y in range(1, m + 1):
    for i in range(22, d + 1):
        d1, d10 = map(int, str(i))
        if d1 < 2 or d10 < 2:
            continue
        if d1 * d10 == y:
            day += 1

print(day)