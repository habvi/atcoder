n = int(input())
S = input()

nxt = list(enumerate(S))
nxt.sort(key=lambda x: (x[1], -x[0]), reverse=True)

ans = list(S)
r = n
for l, s in enumerate(S):
    while nxt and nxt[-1][1] < s:
        i, _ = nxt.pop()
        if l < i < r:
            ans[l], ans[i] = ans[i], ans[l]
            r = i
            break

print(''.join(ans))