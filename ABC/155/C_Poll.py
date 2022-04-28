from collections import Counter

n = int(input())
S = [input() for _ in range(n)]

c = Counter(S)
mx = c.most_common()[0][1]

ans = []
for k, v in c.items():
    if v == mx:
        ans.append(k)

print(*sorted(ans))