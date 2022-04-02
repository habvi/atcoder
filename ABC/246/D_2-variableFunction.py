def calc(a, b):
    return (a + b) * (a**2 + b**2)

def is_ok(b):
    return calc(a, b) >= n

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())

mx = int(n**(1 / 3)) + 1
ans = float('inf')
for a in range(mx + 1):
    b = bisect(-1, mx)
    ans = min(ans, calc(a, b))

print(ans)