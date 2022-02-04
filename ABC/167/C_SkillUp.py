n, m, x = map(int, input().split())
C = []
A = []
for _ in range(n):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = float('inf')
for i in range(1, 1 << n):
    score = [0] * m
    price = 0
    for j in range(n):
        if i >> j & 1:
            price += C[j]
            for k, a in enumerate(A[j]):
                score[k] += a

    if all(s >= x for s in score):
        ans = min(ans, price)

print(ans if ans != float('inf') else -1)