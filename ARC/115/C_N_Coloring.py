def furui(x):
    memo = [0]*(x + 1)
    for i in range(2, x + 1):
        if memo[i]:
            continue
        memo[i] = i
        for j in range(i * i, x + 1, i):
            if memo[j]:
                continue
            memo[j] = i
    return memo


n = int(input())

a = [0] * (n + 1)
a[1] = 1

memo = furui(n)

for i in range(1, n + 1):
    x = i
    cnt = 1
    while x > 1:
        x //= memo[x]
        cnt += 1
    a[i] = cnt
print(*a[1:])