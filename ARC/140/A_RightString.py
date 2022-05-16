from collections import Counter

def solve(w):
    if n % w:
        return

    alph = [Counter() for _ in range(w)]
    for i, s in enumerate(S):
        alph[i % w][s] += 1

    mx = [al.most_common()[0][0] for al in alph]

    total = 0
    for i, s in enumerate(S):
        total += (s != mx[i % w])

    if total <= K:
        print(w)
        exit()


n, K = map(int, input().split())
S = input()

INF = float('inf')
for i in range(1, n + 1):
    solve(i)