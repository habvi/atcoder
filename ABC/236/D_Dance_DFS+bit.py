def dfs(xor, seen):
    global ans
    if seen == (1 << 2 * N) - 1:
        ans = max(ans, xor)
        return

    for f in range(2 * N):
        if not seen >> f & 1:
            seen |= 1 << f
            for s in range(f + 1, 2 * N):
                if not seen >> s & 1:
                    dfs(xor ^ A[f][s], seen | 1 << s)
            break


N = int(input())
A = []
for i in range(2 * N - 1):
    a = [*[0] * (i + 1), *map(int, input().split())]
    A.append(a)

ans = 0
dfs(0, 0)
print(ans)