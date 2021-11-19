n, k = map(int, input().split())
A = sorted([tuple(map(int, input().split())) for _ in range(n)])

num = []
for i in range(n):
    k -= A[i][1]
    if k <= 0:
        print(A[i][0])
        exit()