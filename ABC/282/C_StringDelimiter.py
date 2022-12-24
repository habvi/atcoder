N = int(input())
S = list(input())

change = False
for i in range(N):
    s = S[i]
    if not change and s == '"':
        change = True
        continue
    if change and s == '"':
        change = False
        continue
    if not change and s == ',':
        S[i] = '.'
print(''.join(S))