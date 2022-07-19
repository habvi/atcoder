def sigma_al(a, l):
    return ((a + l) * (l - a + 1)) // 2

def is_ok(x):
    num = 0
    for a in A:
        if a >= x:
            num += (a - x + 1)
    return num <= K

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
bi = bisect(-1, max(A) + 1)

ans = 0
num = 0
for a in A:
    if a >= bi:
        ans += sigma_al(bi, a)
        num += (a - bi + 1)

if K > num:
    ans += (bi - 1) * (K - num)
print(ans)