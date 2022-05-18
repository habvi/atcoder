from collections import defaultdict

def calc(A):
    m = len(A)
    d = defaultdict(lambda : INF)
    for bit in range(1 << m):
        sum_a, sum_b, sum_c = 0, 0, 0
        for i in range(m):
            if bit >> i & 1:
                a, b, c = A[i]
                sum_a += a
                sum_b += b
                sum_c += c
        d[(sum_a, sum_b)] = min(d[(sum_a, sum_b)], sum_c)
    return d

def ceil(a, b):
    return (a + b - 1) // b


n, ma, mb = map(int, input().split())
abc = [tuple(map(int, input().split())) for _ in range(n)]

mid = n // 2
INF = float('inf')
d1 = calc(abc[:mid])
d2 = calc(abc[mid:])

mx = (mid + 1) * 10
ans = INF
for (a, b), c in d1.items():
    ta, tb = ma, mb
    while ta <= mx and tb <= mx:
        a2, b2 = ta - a, tb - b
        ans = min(ans, d2[(a2, b2)] + c)
        ta += ma
        tb += mb
print(ans if ans != INF else -1)