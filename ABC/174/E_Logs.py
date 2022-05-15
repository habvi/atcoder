def is_ok(x):
    cut = 0
    for a in A:
        if a > x:
            cut += a // x
    return cut <= K

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

mx = max(A)
ans = bisect(0, mx + 1)
print(ans)