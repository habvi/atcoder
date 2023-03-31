from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
ans = sum(v // 2 for v in c.values())
print(ans)
