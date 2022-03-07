S = input()
n = len(S)

doubling = [[0] * n for _ in range(33)]
for i, s in enumerate(S):
    doubling[0][i] = (i + 1 if s == 'R' else i - 1)

for k in range(32):
    for i in range(n):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]

ans = [0] * n
for num in doubling[32]:
    ans[num] += 1
print(*ans)