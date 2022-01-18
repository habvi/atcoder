n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) + [i] for i in range(m)]

for a, b in ab:
    mn = float('inf')
    ans = 0
    for c, d, i in cd[::-1]:
        diff = abs(c - a) + abs(d - b)
        if diff <= mn:
            mn = diff
            ans = i + 1
    print(ans)