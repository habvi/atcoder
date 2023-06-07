N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

for i in range(2 * N):
    now = i % N
    nxt = (i + 1) % N
    T[nxt] = min(T[nxt], T[now] + S[now])
print(T)
