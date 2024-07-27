from bisect import bisect_left, bisect_right


def is_ok(x):
    left = bisect_left(A, B - x)
    right = bisect_right(A, B + x)
    return (right - left) >= K


def my_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
for _ in range(Q):
    B, K = map(int, input().split())
    ans = my_bisect(-1, 2 * 10**8 + 1)
    print(ans)
