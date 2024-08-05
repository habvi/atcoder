def is_ok(x):
    total = sum(min(x, a) for a in A)
    return total <= M


def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = bisect(M + 1, 0)
print("infinite" if ans == M else ans)
