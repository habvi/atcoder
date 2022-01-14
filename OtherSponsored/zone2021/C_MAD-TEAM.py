def is_ok(x):
    s = set()
    for p in ab:
        bit = 0
        for i in range(5):
            if p[i] >= x:
                bit |= 1 << i
        s.add(bit)

    for a in s:
        for b in s:
            for c in s:
                if a | b | c  == (1 << 5) - 1:
                    return True
    return False

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ans = bisect(10**9 + 1, 0)
print(ans)