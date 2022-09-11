from itertools import permutations

def dfs(A, res):
    if len(A) == N - 1:
        ub_all.append(A)
        return
    for i in range(1, res + 1):
        dfs(A + [i], res - i)


N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

if N == 1:
    s = S[0]
    print(s if s not in T and len(s) >= 3 else -1)
    exit()

ub_total = 16 - sum(map(len, S))
ub_all = []
dfs([], ub_total)

for per in permutations(S):
    for ub in ub_all:
        s = ""
        for w, u in zip(per, ub + [0]):
            s += w + '_' * u
        if s not in T:
            print(s)
            exit()
print(-1)