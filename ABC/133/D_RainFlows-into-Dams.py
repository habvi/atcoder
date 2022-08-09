N = int(input())
A = list(map(int, input().split()))

x = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        x += a
    else:
        x -= a

print(x, end=' ')
for a in A[:-1]:
    x = 2 * a - x
    print(x, end=' ')