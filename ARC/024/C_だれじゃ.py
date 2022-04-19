from collections import defaultdict

def stoi(s):
    return ord(s) - ord('a')


n, K = map(int, input().split())
S = input()

alph = [0] * 26
for i in range(K):
    alph[stoi(S[i])] += 1

d = defaultdict(lambda : -1)
d[tuple(alph)] = K - 1

for i, s in enumerate(S[K:], K):
    alph[stoi(s)] += 1
    alph[stoi(S[i - K])] -= 1

    new = tuple(alph)
    pre = d[new]
    if pre != -1:
        if (i - pre) >= K:
            print('YES')
            exit()
    else:
        d[new] = i
print('NO')