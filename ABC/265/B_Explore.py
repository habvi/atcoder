N, M, T = map(int, input().split())
A = list(map(int, input().split()))

bonus = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    bonus[x] += y

for i in range(N - 1):
    T -= A[i]
    if T <= 0:
        print("No")
        exit()
    T += bonus[i + 1]
print("Yes")