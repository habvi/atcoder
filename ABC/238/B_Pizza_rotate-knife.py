n = int(input())
A = list(map(int, input().split()))

cut = [0, 360]
now = 0
for a in A:
    now = (now + a) % 360
    cut.append(now)
cut.sort()

ans = 0
for l, r in zip(cut, cut[1:]):
    ans = max(ans, r - l)
print(ans)