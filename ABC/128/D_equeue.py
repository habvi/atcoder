n, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for l in range(n + 1):
    for r in range(l, n + 1):
        if l + n - r > K:
            continue

        mix = [*V[:l], *V[r:]]
        mix.sort(reverse=True)

        res = K - len(mix)
        while res and mix and mix[-1] < 0:
            mix.pop()
            res -= 1

        ans = max(ans, sum(mix))
print(ans)