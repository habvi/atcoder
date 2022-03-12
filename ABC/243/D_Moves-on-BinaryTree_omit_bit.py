n, x = map(int, input().split())
S = input()

T = []
for s in S:
    if s == 'U':
        if T and T[-1] != s:
            T.pop()
            continue
    T.append(s)

for t in T:
    if t == 'U':
        x >>= 1
    elif t == 'R':
        x <<= 1
        x |= 1
    else:
        x <<= 1
print(x)