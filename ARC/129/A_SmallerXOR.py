n, l, r = map(int, input().split())
k = len(bin(n)) - 2
ans = 0
for i in range(k):
    if n>>i & 1:
        kl = 1<<i
        kr = (1<<i + 1) - 1
        if kr < l or kl > r: continue
        ans += min(r, kr) - max(l, kl) + 1
print(ans)