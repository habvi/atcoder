from collections import defaultdict

N = int(input())
S = input()
W = list(map(int, input().split()))

ad = defaultdict(int)
ch = defaultdict(int)
children = 0
for s, w in zip(S, W):
    if s == '1':
        ad[w] += 1
    else:
        ch[w] += 1
        children += 1

adult = 0
ans = children
for w in sorted(set(W), reverse=True):
    adult += ad[w]
    children -= ch[w]
    ans = max(ans, adult + children)
print(ans)
