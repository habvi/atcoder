# https://atcoder.jp/contests/abc163/tasks/abc163_d

def sigma_adn(a, d, n):
    return (2*a + (n - 1)*d) * n // 2


n, K = map(int, input().split())
MOD = 10**9 + 7

ans = 0
for num in range(K, n + 2):
    l = sigma_adn(0, 1, num)
    r = sigma_adn(n, -1, num)
    ans += r - l + 1
    ans %= MOD
print(ans)