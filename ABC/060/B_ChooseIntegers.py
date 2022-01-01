a, b, c = map(int, input().split())
k = a
for i in range(101):
    if k % b == c:
        print('YES')
        exit()
    k += a 
print('NO')