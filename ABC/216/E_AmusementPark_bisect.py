def sigma_al(a, l):
    return ((a + l) * (l - a + 1)) // 2

def is_ok(x):
    total = 0
    for a in A:
        total += max(0, a - x + 1)
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

K = min(K, sum(A))
mx = max(A)
border = bisect(-1, mx + 1)

ans = 0
for a in A:
    if a >= border:
        num = a - border + 1
        ans += sigma_al(border, a)
        K -= num
ans += (border - 1) * K
print(ans)