n, X = map(int, input().split())
S = input()

x = list(bin(X)[2:])

for s in S:
    if s == 'U':
        x.pop()
    elif s == 'R':
        x.append('1')
    else:
        x.append('0')

print(int(''.join(x), 2))