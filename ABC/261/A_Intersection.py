l1, r1, l2, r2 = map(int, input().split())

a = [0] * 101
for i in range(l1, r1 + 1):
    a[i] += 1

for i in range(l2, r2 + 1):
    a[i] += 1

ans = a.count(2)
print(ans - 1 if ans else ans)