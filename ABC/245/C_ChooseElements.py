n, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [A[0], B[0]]
for a, b in zip(A, B):
    nc = set()
    for c in C:
        if abs(a - c) <= K:
            nc.add(a)
        if abs(b - c) <= K:
            nc.add(b)
    C = nc

print('Yes' if C else 'No')