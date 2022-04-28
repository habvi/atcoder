from bisect import bisect

def ceil(a, b):
    return (a + b - 1) // b


n, D, A = map(int, input().split())
xh = [tuple(map(int, input().split())) for _ in range(n)]

xh.sort()
ac = [0] * n

ans = 0
for i, (x, h) in enumerate(xh):
    if i > 0:
        ac[i] += ac[i - 1]

    times = ceil(max(0, h - ac[i]), A)
    ans += times

    ac[i] += A * times

    j = bisect(xh, (x + D * 2, float('inf')))
    if 0 <= j < n:
        ac[j] -= A * times

print(ans)