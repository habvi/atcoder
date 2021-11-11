n = int(input())
a = list(map(int, input().split()))
sm = sum(a)
k = sm//n
if sm == 0:
    print(0)
    exit()
if not (sm >= n and sm%n == 0):
    print(-1)
    exit()

# iの時点での定員外の人数ch。ch==0のとき橋は不要。
ans = 0
ch = 0
for i in a:
    ch += (i - k)
    if ch:
        ans += 1
print(ans)