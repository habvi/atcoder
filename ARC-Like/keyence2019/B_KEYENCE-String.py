S = input()

n = len(S)
for i in range(n):
    for j in range(n):
        T = S[:j] + S[i + j:]
        if T == 'keyence':
            print('YES')
            exit()
print('NO')