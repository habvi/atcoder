N, MOD = map(int, input().split())

ans = []
for num in range(1, 10):
    x = 0
    for i in range(N):
        x = x * 10 + num
        x %= MOD
        if x == 0:
            ans.append((num, (i + 1) * (N // (i + 1))))
            break

ans.sort(key=lambda x: (-x[1], -x[0]))
if ans:
    x, num = ans[0]
    print(str(x) * num)
else:
    print(-1)