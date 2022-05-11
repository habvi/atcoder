def sigma(n):
    return n*(n + 1) // 2

def solve(x):
    if x == 0:
        return 0

    k = 10 ** (len(str(x)) - 1)
    return (sigma(x - k + 1) + solve(k - 1)) % MOD


n = int(input())
MOD = 998244353

print(solve(n))