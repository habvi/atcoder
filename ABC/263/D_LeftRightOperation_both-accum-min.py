def calc(x, A):
    res = [0]
    for i, a in enumerate(A):
        if x * (i + 1) < res[-1] + a:
            res.append(x * (i + 1))
        else:
            res.append(res[-1] + a)
    return res


N, L, R = map(int, input().split())
A = list(map(int, input().split()))

left = calc(L, A)
right = calc(R, A[::-1])[::-1]

ans = float('inf')
for l, r in zip(left, right):
    ans = min(ans, l + r)
print(ans)