from collections import defaultdict

n = int(input())

num = defaultdict(int)
for _ in range(n):
    s = input()
    ans = s
    m = num[s]
    if m >= 1:
        ans += '(' + str(m) + ')'
    num[s] += 1
    print(ans)