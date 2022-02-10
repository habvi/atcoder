def sigma_adn(a, d, n):
    return (2*a + (n - 1)*d) * n // 2


n = int(input())

ans = 0
for i in range(1, n + 1):
    ans += sigma_adn(i, i, n // i)
print(ans)