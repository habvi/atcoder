def is_ok(x):
    lis = []
    for w, p in wp:
        lis.append((w, p, w * (p - x)))
    lis.sort(key=lambda x: -x[2])
    
    tw, salt = 0, 0
    for i in range(k):
        salt += lis[i][0] * lis[i][1] / 100
        tw += lis[i][0]
    return salt / tw * 100 < x

def bisect(ng, ok):
    for _ in range(50):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n, k = map(int, input().split())
wp = [tuple(map(int, input().split())) for _ in range(n)]
bi = bisect(-1, 101)
print(bi)