X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()

ab = []
for a in A:
    for b in B:
        ab.append(a + b)

ab.sort(reverse=True)

total = []
for num in ab[:min(K, len(ab))]:
    for c in C:
        total.append(num + c)

print(*sorted(total, reverse=True)[:K])