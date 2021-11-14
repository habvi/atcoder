def is_ok(x):
    tot = 0
    for a in A:
        tot += min(a, x)
    if tot >= x * k: return True
    else: return False

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = bisect(10**18//k, 0)
print(ans)