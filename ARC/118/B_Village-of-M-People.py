k, n, m = map(int, input().split())
A = list(map(int, input().split()))

B = []
ans = []
for i, a in enumerate(A):
    div = m * a / n
    mod = div % 1

    B.append((mod, i))
    ans.append(int(div))

B.sort(reverse=True)

res = m - sum(ans)
for i in range(res):
    ans[B[i][1]] += 1

print(*ans)