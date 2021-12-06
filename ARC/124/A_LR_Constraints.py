n, K = map(int, input().split())
MOD = 998244353
ng = [set() for _ in range(n)]
ok = [set() for _ in range(n)]
s = [-1] * n
for i in range(K):
    c, k = input().split()
    k = int(k)
    s[k - 1] = k
    if c == 'L':
        for j in range(n):
            if j == k -1: continue
            if j < k - 1:
                ng[j].add(k)
            else:
                ok[j].add(k)
    else:
        for j in range(n):
            if j == k - 1: continue
            if j >= k:
                ng[j].add(k)
            else:
                ok[j].add(k)

ans = 1
for i in range(n):
    if s[i] > 0:
        continue
    ans *= len(ok[i] - ng[i])
    ans %= MOD
print(ans)