from collections import defaultdict

N = int(input())

ans = 0
d = defaultdict(int)
for a in range(1, N):
    for b in range(1, N // a + 1):
        d[a * b] += 1

for a in range(1, N):
    for b in range(1, N // a + 1):
        ans += d[N - a * b]
print(ans)