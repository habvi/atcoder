N, K = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A[:K])
print(total)
for i, a in enumerate(A[K:], K):
    total += a
    total -= A[i - K]
    print(total)