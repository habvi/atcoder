from itertools import groupby

def is_ok1(x):
    # yet, selected
    dp = [INF] * 2
    dp[1] = 0
    for a in A:
        ndp = [INF] * 2
        ndp[0] = dp[1]
        ndp[1] = max(ndp[1], dp[0] + a - x)
        ndp[1] = max(ndp[1], dp[1] + a - x)
        dp = ndp
    return max(dp) >= 0

def bisect1(ng, ok):
    for _ in range(60):
        mid = (ok + ng) / 2
        if is_ok1(mid):
            ok = mid
        else:
            ng = mid
    return ok

def is_ok2(x):
    B = [1 if a >= x else 0 for a in A]
    one = sum(B)
    zero = 0
    for k, v in groupby(B):
        if k == 0:
            zero += len(list(v)) // 2
    return zero <= one - 1

def bisect2(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok2(mid):
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())
A = list(map(int, input().split()))

mx = max(A)
INF = -float('inf')

avrg = bisect1(mx + 1, 0)
med = bisect2(mx + 1, 0)
print(avrg, med)