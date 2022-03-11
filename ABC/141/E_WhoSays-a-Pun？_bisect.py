def is_ok(x):
    exist = set()
    for i in range(n):
        if i + x > n:
            break
        exist.add(S[i : i+x])

        if i + x + x > n:
            break
        if S[i+x : i+x+x] in exist:
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
S = input()

ans = bisect(n + 1, 0)
print(ans)