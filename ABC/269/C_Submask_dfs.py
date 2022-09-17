def dfs(A, res):
    if len(A) == n:
        print(int(''.join(A), 2))
        return
    if not res:
        while len(A) < n:
            A.append('0')
        print(int(''.join(A), 2))
        return
    dfs(A + ['0'], res)
    if S[len(A)] == '1':
        dfs(A + ['1'], res - 1)


X = int(input())

S = bin(X)[2:]
n = len(S)
one = 0
k = X.bit_length()
for i in range(k):
    one += (X >> i & 1)

dfs([], one)