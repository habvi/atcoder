def is_ok(x):
    total = 0
    for a, f in zip(A, F):
        total += a - min(a, x // f)
    return total <= K

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
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

ans = bisect(-1, max(A) * max(F) + 1)
print(ans)