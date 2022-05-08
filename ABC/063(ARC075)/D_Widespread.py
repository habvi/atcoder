def ceil(a, b):
    return (a + b - 1) // b

def is_ok(x):
    total = 0
    for h in H:
        res = max(0, h - B * x)
        total += ceil(res, c)
    return total <= x

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, A, B = map(int, input().split())
H = [int(input()) for _ in range(n)]

c = A - B
ans = bisect(0, 10 ** 9 + 1)
print(ans)