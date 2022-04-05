n = int(input())

ok = set()
num = 0
for i in range(1, 1000):
    num += i
    if num > n:
        break
    ok.add(num)

if n not in ok:
    print('No')
    exit()

K = len(ok) + 1
ans = [[] for _ in range(K)]
num = 1
for i in range(K):
    for j in range(i + 1, K):
        ans[i].append(num)
        ans[j].append(num)
        num += 1

print('Yes')
print(K)
for a in ans:
    print(len(a), *a)