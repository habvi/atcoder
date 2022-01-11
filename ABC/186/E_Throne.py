# 解説放送
def extgcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = extgcd(b, a % b)
    return g, y, x - a//b*y

t = int(input())
for _ in range(t):
    n, s, k = map(int, input().split())
    g, x, y = extgcd(k, n)
    if s % g:
        print(-1)
        continue
    n //= g
    s //= g
    k //= g
    ans = ((x * -s) % n + n) % n
    print(ans)