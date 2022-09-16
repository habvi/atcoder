n, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = set([A[0], B[0]])
for a, b in zip(A, B):
    ndp = set()
    for x in dp:
        if abs(a - x) <= K:
            ndp.add(a)
        if abs(b - x) <= K:
            ndp.add(b)
    dp = ndp
print("Yes" if dp else "No")