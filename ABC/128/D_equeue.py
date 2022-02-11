n, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for i in range(n + 1):
    for j in range(n + 1):
        l = i
        r = n - j
        if l > r or i + j > K:
            continue

        merge = [*V[:l], *V[r:]]
        merge.sort(reverse=True)

        res = K - (i + j)
        while merge and res > 0 and merge[-1] < 0:
            merge.pop()
            res -= 1

        ans = max(ans, sum(merge))
print(ans)