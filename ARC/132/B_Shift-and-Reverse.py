n = int(input())
p = list(map(int, input().split()))
if p[0] == 1 and p[-1] == n:
    print(0)
    exit()

mn = p.index(1)
mx = p.index(n)
if mx < mn:
    ans = min(mx + 1, n - mn + 2)
else:
    ans = min(mn + 2, n - mx + 1)
print(ans)