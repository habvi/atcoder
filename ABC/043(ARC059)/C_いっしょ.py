n = int(input())
a = list(map(int, input().split()))
ans = float('inf')
for x in range(min(a), max(a) + 1):
    c = 0
    for i in range(n):
        c += (a[i] - x) ** 2
    ans = min(ans, c)
print(ans)
