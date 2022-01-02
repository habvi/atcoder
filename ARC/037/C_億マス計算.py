from bisect import bisect
n, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

def is_ok(x):
    tot = 0
    for i in range(n):
        tot += bisect(b, x // a[i])
    return tot >= K

def bisect2(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

bi = bisect2(0, a[-1] * b[-1] + 1)
print(bi)