def sigma(x, n):
    return x * n*(n - 1)//2

def is_ok(y, pre, x):
    return pre + x*y > 0 

def bisect(ng, ok, pre, x):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, pre, x):
            ok = mid
        else:
            ng = mid
    return ok


def solve():
    n, _ = map(int, input().split())

    B = [0, 0]
    A = [0]
    ans = -float('inf')
    for i in range(n):
        x, y = map(int, input().split())

        a_left = A[-1] + B[i + 1] + x
        a_right = A[-1] + (B[i + 1] + x)*y + sigma(x, y)
        ans = max(ans, a_left, a_right)

        if x < 0 and B[-1] > 0:
            ny = bisect(y + 1, 0, B[-1], x)
            if 0 < ny < y:
                na = A[-1] + (B[i + 1] + x)*ny + sigma(x, ny)
                ans = max(ans, na)

        B.append(B[-1] + x*y)
        A.append(a_right)
    return ans


T = int(input())
for _ in range(T):
    print(solve())