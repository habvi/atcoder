def ceil(a, b):
    return (a + b - 1) // b

def is_ok(x):
    plus = 0
    B = []
    for a in A:
        if a < x:
            times = ceil((x - a), p)
            plus += times
            B.append(a + p * times)
        else:
            B.append(a)
    minus = 0
    for b in B:
        minus += (b - x) // m
    return plus <= minus

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, p, m = map(int, input().split())
A = list(map(int, input().split()))

mx = max(A)
bi = bisect(mx + 1, 0)
print(bi)