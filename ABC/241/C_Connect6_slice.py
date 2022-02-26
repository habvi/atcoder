n = int(input())
S = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        a = S[i][j : j + 6]
        if a.count('#') >= 4:
            print('Yes')
            exit()

for t in zip(*S):
    for i in range(n):
        a = t[i : i + 6]
        if a.count('#') >= 4:
            print('Yes')
            exit()

for i in range(n - 5):
    for j in range(n - 5):
        l = 0
        for k in range(6):
            if S[i + k][j + k] == '#':
                l += 1
        if l >= 4:
            print('Yes')
            exit()

        r = 0
        for k in range(6):
            if S[i + k][j + 5 - k] == '#':
                r += 1
        if r >= 4:
            print('Yes')
            exit()

print('No')