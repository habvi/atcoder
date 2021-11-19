n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in [i, i+1]:
        if a[j] <= b[i]:
            ans += a[j]
            mn = a[j]
        else:
            ans += b[i]
            mn = b[i]
        a[j] -= mn
        b[i] -= mn
print(ans)