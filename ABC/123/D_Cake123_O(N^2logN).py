x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
lis = []
for i in range(x):
    for j in range(y):
        lis.append(a[i] + b[j])

lis.sort(reverse=True)
c.sort(reverse=True)
ans = []
for i in range(min(k, len(lis))):
    for j in range(z):
        ans.append(lis[i] + c[j])
ans.sort(reverse=True)
print(*ans[:k])