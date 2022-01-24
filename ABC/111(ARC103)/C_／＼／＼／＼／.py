from collections import Counter

n = int(input())
V = list(map(int, input().split()))

odd = Counter()
even = Counter()
for i, v in enumerate(V):
    if i % 2:
        odd[v] += 1
    else:
        even[v] += 1

ans = float('inf')
o1, a = odd.most_common(1)[0]
for k, v in even.items():
    if o1 == k:
        continue
    ans = min(ans, n // 2 - a + n // 2 - v)

e1, a = even.most_common(1)[0]
for k, v in odd.items():
    if e1 == k:
        continue
    ans = min(ans, n // 2 - a + n // 2 - v)

if len(set(V)) == 1:
    ans = n // 2
print(ans)