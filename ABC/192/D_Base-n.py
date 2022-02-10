def n_to_deci(X, base):
    num = 0
    for x in X:
        num = num * base + x
    return num

def is_ok(x):
    return n_to_deci(ls, x) <= M

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


S = input()
M = int(input())

if len(S) == 1:
    print(0 if int(S) > M else 1)
    exit()

ls = [int(s) for s in S]
d = max(ls)

bi = bisect(M + 1, d)
print(bi - d)