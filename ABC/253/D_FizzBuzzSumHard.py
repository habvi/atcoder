from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def sigma_adn(a, d, n):
    return (2*a + (n - 1)*d) * n // 2


n, A, B = map(int, input().split())

ans = sigma_adn(1, 1, n)
ans -= sigma_adn(B, B, n // B)
ans -= sigma_adn(A, A, n // A)
l = lcm(A, B)
ans += sigma_adn(l, l, n // l)
print(ans)