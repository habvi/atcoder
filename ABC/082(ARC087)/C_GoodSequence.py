from collections import Counter

n = int(input())
A = list(map(int, input().split()))

ans = 0
for k, v in Counter(A).items():
    ans += (v - k if v >= k else v)
print(ans)