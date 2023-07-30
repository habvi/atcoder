def is_ok(x):
    sell = sum(x >= a for a in A)
    buy = sum(x <= b for b in B)
    return sell >= buy

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
B = list(map(int, input().split()))

mx = max(max(A), max(B))
ans = bisect(0, mx + 1)
print(ans)
