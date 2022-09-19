n = int(input())

total = 0
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    total += a / b
    ab.append((a, b))

half = total / 2
ans = 0
for a, b in ab:
    t = a / b
    if t < half:
        half -= t
        ans += a
    else:
        ans += half * b
        break
print(ans)