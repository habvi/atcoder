S = input()[:-1]
n = len(S)

for i in reversed(range(1, n // 2 + 1)):
    if S[:i] == S[i:i * 2]:
        print(i * 2)
        exit()