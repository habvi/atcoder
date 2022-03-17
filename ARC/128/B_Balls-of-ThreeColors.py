def check(a, b, c):
    if b > c:
        b, c = c, b
    c -= b

    total = b
    if c == 0:
        return total

    if c % 3:
        return float('inf')

    total += c
    return total


T = int(input())
for _ in range(T):
    r, g, b = map(int, input().split())

    ans = float('inf')
    ans = min(ans, check(r, g, b))
    ans = min(ans, check(g, b, r))
    ans = min(ans, check(b, r, g))

    print(ans if ans != float('inf') else -1)