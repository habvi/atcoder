def is_ok(x):
    inc = 0
    for a in A:
        if a > x:
            inc += a // x
    return inc <= K

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, K = map(int, input().split())
A = list(map(int, input().split()))

ans = bisect(0, 10**9 + 1)
print(ans)