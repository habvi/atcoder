n = int(input())

ok = {'TAKAHASHIKUN', 'Takahashikun', 'takahashikun'}
ans = 0
for i, w in enumerate(input().split()):
    if i == n - 1:
        w = w[:-1]
    ans += (w in ok)

print(ans)