from collections import defaultdict

N = int(input())

pair = defaultdict(int)
for i in range(1, N + 1):
    s = str(i)
    pair[(s[0], s[-1])] += 1

ans = 0
for a in range(1, N + 1):
    s = str(a)
    ans += pair[(s[-1], s[0])]
print(ans)
