def check(S):
    res = [0] * n
    i = 0
    while i < n:
        if S[i] == 'x':
            i += 1
            continue
        res[i] = 1
        i += C + 1
    return res


n, K, C = map(int, input().split())
S = input()

left = check(S)
right = check(S[::-1])[::-1]

if sum(left) > K or sum(right) > K:
    exit()

for i, (l, r) in enumerate(zip(left, right), 1):
    if l and r:
        print(i)