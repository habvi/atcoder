def sigma(n):
    return n*(n + 1) // 2


n, K = map(int, input().split())

if sigma(n - 2) < K:
    print(-1)
    exit()

ans = []
for i in range(2, n + 1):
    ans.append((1, i))

total = sigma(n - 2)

for i in range(2, n + 1):
    for j in range(i + 1, n + 1):
        if total <= max(K, 0):
            break
        ans.append((i, j))
        total -= 1
    else:
        continue
    break

print(len(ans))
for u, v in ans:
    print(u, v)