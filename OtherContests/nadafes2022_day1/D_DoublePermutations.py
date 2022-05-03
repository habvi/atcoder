n = int(input())

if n == 1:
    print(0)
    exit()

if n % 2:
    print(-1)
    exit()

mod = []
for i in range(n, n // 2, -1):
    mod.append(i % n)
    mod.append(n + 1 - i)

ans = [0]
pre = 0
for m in mod[1:]:
    nxt = (n + m - pre) % n
    ans.append(nxt)
    pre = m
print(*ans)