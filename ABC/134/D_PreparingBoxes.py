n = int(input())
a = [0]
a.extend(list(map(int, input().split())))
b = [0] * (n + 1)
ans = []
for i in range(n, 0, -1):
    cnt = 0
    for j in range(i, n + 1, i):
        cnt += b[j]
    
    if cnt % 2 == a[i]:
        b[i] = 0
    else:
        b[i] = 1
        ans.append(i)

print(len(ans))
print(*ans)