S = input()

n = len(S)
INF = float('inf')
ans = INF
for bit in range(1, 1 << n):
    total = 0
    rm = 0
    for i in range(n):
        if bit >> i & 1:
            total += int(S[i])
        else:
            rm += 1
    if total % 3 == 0 and rm != n:
        ans = min(ans, rm)
print(ans if ans != INF else -1)
