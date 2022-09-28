N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

for i in range(2 * N):
    T[(i + 1) % N] = min(T[(i + 1) % N], T[i % N] + S[i % N])
print(*T)