N = int(input())
A = [list(input()) for _ in range(N)]

idx = []
nums = []
for j in range(N):
    i = 0
    idx.append((i, j))
    nums.append(A[i][j])
for i in range(1, N - 1):
    j = N - 1
    idx.append((i, j))
    nums.append(A[i][j])
for j in reversed(range(N)):
    i = N - 1
    idx.append((i, j))
    nums.append(A[i][j])
for i in reversed(range(1, N - 1)):
    j = 0
    idx.append((i, j))
    nums.append(A[i][j])

for (i, j), x in zip(idx, [nums[-1]] + nums[:-1]):
    A[i][j] = x
for a in A:
    print(''.join(a))