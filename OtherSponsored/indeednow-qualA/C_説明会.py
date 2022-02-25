n = int(input())
S = []
for _ in range(n):
    s = int(input())
    if s:
        S.append(s)

S.append(-1)
S.sort(reverse=True)

q = int(input())
for _ in range(q):
    k = int(input())
    k = min(k, len(S) - 1)

    print(S[k] + 1)