n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)

if n < m:
    print('NO')
    exit()

for i in range(min(n, m)):
    if a[i] < b[i]:
        print('NO')
        exit()
print('YES')