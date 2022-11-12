from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += a

ks = sorted(d.keys())
seq = []
left = 0
for i in range(len(ks) - 1):
    if ks[i] + 1 == ks[i + 1]:
        continue
    right = i
    seq.append((left, right))
    left = i + 1
seq.append((left, len(ks) - 1))

total = sum(A)
seq_sum = []
ans = float('inf')
for l, r in seq:
    s_sum = sum(d[ks[i]] for i in range(l, r + 1))
    ans = min(ans, total - s_sum)
    seq_sum.append(s_sum)

if (ks[0] == 0) and (ks[-1] == M - 1) and (len(seq_sum) >= 2):
    ans = min(ans, total - seq_sum[0] - seq_sum[-1])
print(ans)