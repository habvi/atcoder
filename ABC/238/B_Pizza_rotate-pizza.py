n = int(input())
A = list(map(int, input().split()))

S = []
for a in A:
    S.append(0)
    T = []
    for s in S:
        T.append((s + a) % 360)
    S = T

S = [0, *sorted(S), 360]

ans = 0
for i in range(len(S) - 1):
    ans = max(ans, S[i + 1] - S[i])
print(ans)