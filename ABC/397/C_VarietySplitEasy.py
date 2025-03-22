from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

left = defaultdict(int)
right = defaultdict(int)
for a in A:
    right[a] += 1

l_max = 0
r_max = len(right)
ans = r_max
for a in A:
    right[a] -= 1
    if not right[a]:
        del right[a]
        r_max -= 1
    if a not in left:
        l_max += 1
    left[a] += 1
    ans = max(ans, l_max + r_max)
print(ans)
