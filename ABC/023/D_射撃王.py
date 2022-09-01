def is_ok(x):
    T = []
    for h, s in hs:
        if x - h < 0:
            return False
        T.append((x - h) // s)
    T.sort()
    for i, t in enumerate(T):
        if t < i:
            return False
    return True

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
hs = [tuple(map(int, input().split())) for _ in range(N)]

mx = 10**9 + N * 10**9
ans = bisect(0, mx + 1)
print(ans)
