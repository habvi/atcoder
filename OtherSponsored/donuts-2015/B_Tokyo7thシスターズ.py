n, m = map(int, input().split())
A = tuple(map(int, input().split()))

B = []
P = []
for _ in range(m):
    b, c, *p = map(int, input().split())
    B.append(b)
    P.append(set(p))

ans = 0
for bit in range(1 << n):
    if bin(bit).count('1') != 9:
        continue

    selected = set()
    base = 0
    for i, a in enumerate(A):
        if bit >> i & 1:
            selected.add(i + 1)
            base += a

    bonus = 0
    for i, (p, b) in enumerate(zip(P, B)):
        if len(p & selected) >= 3:
            bonus += b

    ans = max(ans, base + bonus)

print(ans)