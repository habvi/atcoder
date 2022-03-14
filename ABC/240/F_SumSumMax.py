def sigma(x, n):
    return x * n*(n + 1)//2

def solve():
    n, _ = map(int, input().split())

    B = [0]
    A = [0]
    ans = -float('inf')
    for _ in range(n):
        x, y = map(int, input().split())
        a, b = A[-1], B[-1]

        a_left = a + b + x
        a_right = a + b*y + sigma(x, y)
        ans = max(ans, a_left, a_right)

        if x < 0 and b > 0:
            ny = b // -x
            if 0 < ny < y:
                na = a + b*ny + sigma(x, ny)
                ans = max(ans, na)

        B.append(b + x*y)
        A.append(a_right)
    return ans


T = int(input())
for _ in range(T):
    print(solve())