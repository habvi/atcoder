N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N - 5):
        c = S[i][j:j + 6].count('.')
        if c <= 2:
            print("Yes")
            exit()

for s in zip(*S):
    for i in range(N - 5):
        c = s[i:i + 6].count('.')
        if c <= 2:
            print("Yes")
            exit()

for i in range(N - 5):
    for j in range(N - 5):
        c1, c2 = 0, 0
        for k in range(6):
            c1 += (S[i + k][j + k] == '.')
            c2 += (S[i + k][j + 5 - k] == '.')
        if c1 <= 2 or c2 <= 2:
            print("Yes")
            exit()
print("No")