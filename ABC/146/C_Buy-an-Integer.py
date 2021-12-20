def is_ok(n):
    return a*n + b*len(str(n)) <= x

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

a, b, x = map(int, input().split())
bi = bisect(10**9 + 1, 0)
print(bi)