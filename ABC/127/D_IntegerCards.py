from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))

cand = Counter(A)

for _ in range(m):
    b, c = map(int, input().split())
    cand[c] += b

ans = 0
for k in sorted(cand.keys(), reverse=True):
    num = cand[k]
    if n > 0:
        ans += k * min(n, num)
        n -= num
    else:
        break

print(ans)