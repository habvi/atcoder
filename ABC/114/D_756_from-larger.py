from collections import defaultdict

def comb(n):
    return n * (n - 1) // 2


n = int(input())

div = defaultdict(int)
for x in range(1, n + 1):
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x //= i
            div[i] += 1
    if x >= 2:
        div[x] += 1

s = [0] * 5
for k, v in div.items():
    for i, x in enumerate((2, 4, 14, 24, 74)):
        if v >= x:
            s[i] += 1

ans = comb(s[1]) * (s[0] - 2)
for i, j in [(0, 3), (1, 2)]:
    ans += s[j] * (s[i] - 1)
ans += s[4]

print(ans)