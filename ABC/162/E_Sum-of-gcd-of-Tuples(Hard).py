def exclude_duplicate_divisor(x):
    div = [0] * (x + 1)
    for i in reversed(range(1, x + 1)):
        num = K // i
        div[i] = pow(num, n, MOD)
        for ex in range(i + i, x + 1, i):
            div[i] -= div[ex]
    return div


n, K = map(int, input().split())
MOD = 10**9 + 7

div = exclude_duplicate_divisor(K)

ans = 0
for i, num in enumerate(div):
    ans += i * num
    ans %= MOD

print(ans)