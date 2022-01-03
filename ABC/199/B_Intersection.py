n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mn = 0
mx = float('inf')
for i in range(n):
    mn = max(mn, a[i])
    mx = min(mx, b[i])
print(max(0, mx - mn + 1))