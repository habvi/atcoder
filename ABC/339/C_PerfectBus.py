N = int(input())
A = list(map(int, input().split()))

mn = 0
now = 0
for a in A:
    now += a
    mn = min(mn, now)

print(now - mn)