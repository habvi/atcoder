def stoi(s):
    return ord(s) - ord('a')

def itos(i):
    return chr(i + ord('a'))

def calc(x):
    if n % x:
        return n

    alph = [[0] * 26 for _ in range(x)]
    for i, s in enumerate(S):
        alph[i % x][stoi(s)] += 1

    mx = []
    for al in alph:
        i = al.index(max(al))
        mx.append(itos(i))

    total = 0
    for i, s in enumerate(S):
        if s != mx[i % x]:
            total += 1
    if total <= K:
        return x
    else:
        return n

n, K = map(int, input().split())
S = input()

INF = float('inf')
ans = n
for i in range(1, n + 1):
    ans = min(ans, calc(i))
print(ans)