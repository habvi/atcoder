n = int(input())
if n == 1:
    print(0)
    exit()

a = [list(map(int, input().split())) for _ in range(n - 1)]
for i in range(n - 1):
    t = 0
    for j in range(i, n - 1):
        c, s, f = a[j]
        if t <= s:
            t = s + c
            continue
        if (t - s) % f == 0:
            t += c
            continue
        b = ((t - s) + f - 1) // f
        t = s + f * b + c
    print(t)
print(0)