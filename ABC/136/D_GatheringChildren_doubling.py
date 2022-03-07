from math import log2

S = input()
n = len(S)

m = int(log2(10 ** 5)) + 1

doubling = [[0] * n for _ in range(m + 1)]
for i, s in enumerate(S):
    doubling[0][i] = (i + 1 if s == 'R' else i - 1)

for k in range(m):
    for i in range(n):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]

ans = [0] * n
for num in doubling[m]:
    ans[num] += 1
print(*ans)