def is_ok(x):
    total = 0
    for a in A:
        total += min(a, x)
    return total <= K

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N, K = map(int, input().split())
A = list(map(int, input().split()))

loop = bisect(K + 1, 0)
total = 0
for i in range(N):
    total += min(A[i], loop)
    A[i] = max(0, A[i] - loop)

K -= total
for i in range(N):
    if not K:
        break
    if A[i]:
        A[i] -= 1
        K -= 1
print(*A)
