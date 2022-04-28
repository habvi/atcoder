S = input()

n = len(S)
for i in range(n - 1):
    if S[i] == S[i + 1]:
        print(i + 1, i + 2)
        exit()

    if i + 2 < n and S[i] == S[i + 2]:
        print(i + 1, i + 3)
        exit()

print(-1, -1)