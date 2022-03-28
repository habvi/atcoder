def dfs(i, bamboo):
    global ans
    if i == n:
        if not bamboo[0] or not bamboo[1] or not bamboo[2]:
            return

        total = 0
        for bam, target in zip(bamboo, (A, B, C)):
            total += (len(bam) - 1) * 10
            total += abs(sum(bam) - target)
        ans = min(ans, total)
        return

    dfs(i + 1, bamboo)

    for j in range(3):
        bamboo[j].append(L[i])
        dfs(i + 1, bamboo)
        bamboo[j].pop()


n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]

ans = float('inf')
dfs(0, [[] for _ in range(3)])
print(ans)