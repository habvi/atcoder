n, A, B = map(int, input().split())
V = list(map(int, input().split()))

V.sort()
total = sum(V[-A:])
average = total / A
print(average)

comb = [[0] * (n + 1) for _ in range(n + 1)]
comb[0][0] = 1
for i in range(n):
    for j in range(i + 1):
        comb[i + 1][j] += comb[i][j]
        comb[i + 1][j + 1] += comb[i][j]

mn = V[-A]
mn_total = 0
mn_num = 0
for i, v in enumerate(V):
    mn_total += (v == mn)
    if i >= n - A:
        mn_num += (v == mn)

if V[-1] == mn:
    ans = 0
    for i in range(A, B + 1):
        ans += comb[mn_total][i]
else:
    ans = comb[mn_total][mn_num]
print(ans)