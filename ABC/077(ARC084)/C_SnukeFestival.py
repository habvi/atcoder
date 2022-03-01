from bisect import bisect, bisect_left
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
c.sort()
ans = 0
for x in b:
    ans += bisect_left(a, x) * (n - bisect(c, x))
print(ans)