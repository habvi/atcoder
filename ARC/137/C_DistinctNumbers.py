n = int(input())
A = [-1, *map(int, input().split())]

d = 0
for i in range(n):
    d += A[i + 1] - A[i] - 1

print('Bob' if d % 2 == 0 and A[-2] + 1 == A[-1] else 'Alice')