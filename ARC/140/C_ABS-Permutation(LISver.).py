def make():
    m = len(A)
    mid = m // 2
    i = mid
    dist = 1
    while 0 <= i <= m - 1:
        ans.append(A[i])
        if i >= mid:
            i -= dist
        else:
            i += dist
        dist += 1


n, X = map(int, input().split())

A = list(range(1, n + 1))
center = (n + 1) // 2
ans = []
if (n % 2 and X != center) or (not n % 2 and X not in (center, center + 1)):
    ans.append(X)
    A.pop(X - 1)

make()
print(*ans)