h, w, K = map(int, input().split())
S = [input() for _ in range(h)]

ans = 0
for r in range(1 << h):
    for c in range(1 << w):
        total = 0
        for i in range(h):
            if not r >> i & 1:
                continue
            for j in range(w):
                if not c >> j & 1:
                    continue
                total += (S[i][j] == '#')
        ans += (total == K)
print(ans)