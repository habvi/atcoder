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

s = [set() for _ in range(5)]
for k, v in div.items():
    for i, x in enumerate((2, 4, 14, 24, 74)):
        if v >= x:
            s[i].add(k)

ans = 0
for x in s[0]:
    k = len(s[1] - {x})
    if k >= 2:
        ans += comb(k)

for i, j in [(0, 3), (1, 2)]:
    for x in s[i]:
        k = len(s[j] - {x})
        ans += k

ans += len(s[4])
print(ans)