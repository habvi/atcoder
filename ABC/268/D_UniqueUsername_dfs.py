from itertools import permutations

def dfs(A):
    if len(A) == N - 1:
        if sum(A) <= ub_total:
            ub_all.append(A)
        return
    for i in range(1, ub_total):
        dfs(A + [i])


N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

if N == 1:
    print(S[0] if S[0] not in T and len(S[0]) >= 3 else -1)
    exit()

ub_total = 16 - sum(map(len, S))
ub_all = []
for i in range(1, ub_total + 1):
    dfs([i])

for per in permutations(S):
    for ub in ub_all:
        s = ""
        for w, u in zip(per, list(ub) + [0]):
            s += w + '_' * u
        if s not in T:
            print(s)
            exit()
print(-1)