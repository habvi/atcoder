H, W = map(int, input().split())
C = ["." * (W + 2)] + ["." + input() + "." for _ in range(H)] + ["." * (W + 2)]

N = min(H, W)
ans = [0] * N
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if C[i][j] != '#':
            continue
        d = 1
        ok = False
        while i + d <= H and i - d >= 1 and j + d <= W and j - d >= 1:
            if C[i + d][j + d] == C[i + d][j - d] == C[i - d][j + d] == C[i - d][j - d] == '#':
                d += 1
                ok = True
            else:
                break
        if ok:
            ans[d - 2] += 1
print(*ans)
