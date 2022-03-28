def dfs(i, num, length):
    global ans
    if i == n:
        if 0 in num:
            return

        total = 0
        for m, l, target in zip(num, length, (A, B, C)):
            total += (m - 1) * 10
            total += abs(l - target)
        ans = min(ans, total)
        return

    dfs(i + 1, num, length)

    for j in range(3):
        num[j] += 1
        length[j] += L[i]
        dfs(i + 1, num, length)
        num[j] -= 1
        length[j] -= L[i]


n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]

ans = float('inf')
dfs(0, [0] * 3, [0] * 3)
print(ans)