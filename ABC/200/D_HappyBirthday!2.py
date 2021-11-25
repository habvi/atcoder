n = int(input())
A = list(map(int, input().split()))
MOD = 200

m = min(n, 8)
for i in range(1, 1<<m):
    for j in range(1, 1<<m):
        if i == j: continue
        b, c = [], []
        sum_b, sum_c = 0, 0
        for k in range(m):
            if (i>>k) & 1:
                b.append(k + 1)
                sum_b += A[k]
                sum_b %= MOD
            if (j>>k) & 1:
                c.append(k + 1)
                sum_c += A[k]
                sum_c %= MOD
        if sum_b == sum_c:
            print('Yes')
            print(len(b), *b)
            print(len(c), *c)
            exit()
print('No')