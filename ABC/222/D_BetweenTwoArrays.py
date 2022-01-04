n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 998244353

if n == 1:
    print(b[0] - a[0] + 1)
    exit()

c = [0] * 3001
for i in range(a[-2], b[-2] + 1):
    c[i] = b[-1] - max(a[-1], i) + 1

if n == 2:
    print(sum(c))
    exit()

for i in range(b[-2], a[-2], -1):
    c[i - 1] += c[i] % MOD
ac = c

for i in range(n - 3, -1, -1):
    c = [0] * 3001
    for j in range(a[i], b[i] + 1):
        idx = max(j, a[i + 1])
        c[j] = ac[idx]

    for j in range(b[i], a[i], -1):
        c[j - 1] += c[j] % MOD
    ac = c
print(ac[a[0]] % MOD)