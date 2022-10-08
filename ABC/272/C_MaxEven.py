N = int(input())
A = list(map(int, input().split()))

odd, even = [], []
for a in A:
    if a % 2:
        odd.append(a)
    else:
        even.append(a)

odd.sort()
even.sort()
ans = -1
if len(odd) >= 2:
    ans = max(ans, sum(odd[-2:]))
if len(even) >= 2:
    ans = max(ans, sum(even[-2:]))
print(ans)