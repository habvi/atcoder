def itoc(i):
    return chr(i + ord('a'))

N = 8
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if S[i][j] == '*':
            print(itoc(j) + str(N - i))
            exit()
