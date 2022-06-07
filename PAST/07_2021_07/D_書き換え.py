n = int(input())
S = input()

T = '...'
for s in 'aiueo':
    s = s + 'x' + s
    S = S.replace(s, T)
print(S)