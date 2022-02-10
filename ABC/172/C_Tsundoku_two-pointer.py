n, m, K = map(int, input().split())
A = [0, *map(int, input().split())]
B = list(map(int, input().split()))

ans = 0
total = sum(B)
for i, a in enumerate(A):
    if a > K:
        break
    total += a

    while B and total > K:
        rm = B.pop()
        total -= rm

    if total <= K:
        ans = max(ans, len(B) + i)
print(ans)