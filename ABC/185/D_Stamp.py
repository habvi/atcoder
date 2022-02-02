n, m = map(int, input().split())
if not m:
    print(1)
    exit()

A = sorted(map(int, input().split()))
if A[0] != 1:
    A = [0, *A]
if A[-1] != n:
    A.append(n + 1)

la = len(A)
mn = float('inf')
for i in range(la - 1):
    if A[i + 1] - A[i] > 1:
        mn = min(mn, A[i + 1] - A[i] - 1)

if mn == float('inf'):
    print(0)
    exit()

ans = 0
for i in range(la - 1):
    nmr = A[i + 1] - A[i] - 1
    ans += (nmr + mn - 1) // mn
print(ans)