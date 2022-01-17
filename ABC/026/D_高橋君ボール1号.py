from math import sin, pi

def is_ok(x):
    return a * x + b * sin(c * x * pi) >= 100

def bisect(ng, ok):
    for _ in range(100):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

a, b, c = map(int, input().split())
ans = bisect(-1, 10 ** 6)
print(ans)