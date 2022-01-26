n = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

s = set()
ans = 0
for i, a in enumerate(A):
    if i > a:
        i, a = a, i
    if (i, a) in s:
        ans += 1
    else:
        s.add((i, a))
print(ans)