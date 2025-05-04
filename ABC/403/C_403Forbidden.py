from collections import defaultdict

N, M, Q = map(int, input().split())

all_perm = [False] * (N + 1)
partial_perm = defaultdict(set)
for _ in range(Q):
    q, *args = map(int, input().split())
    if q == 1:
        X, Y = args
        partial_perm[X].add(Y)
    elif q == 2:
        X = args[0]
        all_perm[X] = True
    else:
        X, Y = args
        print("Yes" if all_perm[X] or Y in partial_perm[X] else "No")
