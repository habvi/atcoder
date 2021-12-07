n = int(input())
A = list(map(int, input().split()))
ans = -float('inf')
for t in range(n):
    lis = []
    for a in range(n):
        if t == a:
            continue
        l, r = min(t, a), max(t, a)
        tp, ap = 0, 0
        for i, k in enumerate(range(l, r + 1)):
            if i % 2 == 0:
                tp += A[k]
            else:
                ap += A[k]
        lis.append((tp, ap, a))
    lis.sort(key=lambda x : (-x[1], x[2]))
    ans = max(ans, lis[0][0])
print(ans)