n, A, B = map(int, input().split())

now = 0
for _ in range(n):
    s, d = input().split()
    d = int(d)
    if s == 'East':
        now += min(B, max(A, d))
    else:
        now -= min(B, max(A, d))

if now == 0:
    print(0)
elif now > 0:
    print('East', now)
else:
    print('West', -now)