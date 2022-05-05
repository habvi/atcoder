from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

num = defaultdict(int)
ans = 0
for i, a in enumerate(A):
    ans += i - num[a]
    num[a] += 1
print(ans)