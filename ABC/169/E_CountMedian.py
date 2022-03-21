from statistics import median

n = int(input())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()
mn = median(A)
mx = median(B)

diff = mx - mn
print(diff + 1 if n % 2 else int(diff*2) + 1)