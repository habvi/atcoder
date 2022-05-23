def is_ok(x):
    total = 0
    for a, b, c in abc:
        if x < b:
            continue
        total += min(a, (x - b) // c + 1)
    return total < K

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, K = map(int, input().split())
abc = [tuple(map(int, input().split())) for _ in range(n)]

mx = 10**32
ans = bisect(mx, 0)
print(ans + 1)