S = input()
T = input()
n = len(S)
m = len(T)
NG = 'UNRESTORABLE'

cand = []
for i in reversed(range(n - m + 1)):
    ok = True
    for s, t in zip(S[i : i + m], T):
        if s == t or s == '?':
            continue
        ok = False
        break

    if ok:
        C = list(S)
        C[i : i + m] = T
        C = ['a' if c == '?' else c for c in C]
        cand.append(''.join(C))

cand.sort()
print(cand[0] if cand else NG)