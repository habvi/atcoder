def ceil(a, b):
    return (a + b - 1) // b

def is_ok(x):
    plus = 0
    for a in A:
        if a < x:
            plus += ceil((x - a), P)

    minus = 0
    for a in A:
        if a > x:
            minus += (a - x) // M
    return plus <= minus

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, P, M = map(int, input().split())
A = list(map(int, input().split()))

mx = max(A)
bi = bisect(mx + 1, 0)
print(bi)