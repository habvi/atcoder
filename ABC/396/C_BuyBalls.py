from itertools import accumulate

N, M = map(int, input().split())
B = sorted(map(int, input().split()), reverse=True)
W = sorted(map(int, input().split()), reverse=True)

ac_b = list(accumulate(B))
ac_w = list(accumulate(W))
ans = 0
w_max = 0
for i, b in enumerate(ac_b):
    if i < M:
        w_max = max(w_max, ac_w[i])
    total = b + w_max
    ans = max(ans, total)
print(ans)
