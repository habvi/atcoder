N = int(input())
S = list(input())
Q = int(input())

change_all = []
alph_case = 0
last_change = -1
for i in range(Q):
    t, x, c = input().split()
    t, x = int(t), int(x) - 1
    if t == 1:
        change_all.append((i, x, c))
    elif t == 2:
        alph_case = 1
        last_change = i
    else:
        alph_case = 2
        last_change = i

if alph_case == 1:
    for i, s in enumerate(S):
        S[i] = s.lower()
elif alph_case == 2:
    for i, s in enumerate(S):
        S[i] = s.upper()

for (i, xi, c) in change_all:
    if i > last_change:
        S[xi] = c
    else:
        if alph_case == 1:
            S[xi] = c.lower()
        else:
            S[xi] = c.upper()
print(''.join(S))
