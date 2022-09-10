from itertools import combinations, permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

if N == 1:
    s = S[0]
    print(s if s not in T and len(s) >= 3 else -1)
    exit()

ub_total = 16 - sum(map(len, S))
ub_all = []
for com in combinations(range(1, ub_total + 1), N - 1):
    com = [0, *com]
    tmp = []
    for i in range(N - 1):
        tmp.append(com[i + 1] - com[i])
    ub_all.append(tmp)

for per in permutations(S):
    for ub in ub_all:
        s = ""
        for w, u in zip(per, ub + [0]):
            s += w + '_' * u
        if s not in T:
            print(s)
            exit()
print(-1)