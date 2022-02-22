def Sieve(x):
    memo = [0] * (x + 1)
    for i in range(2, x + 1):
        if not memo[i]:
            memo[i] = i
            for j in range(i * i, x + 1, i):
                if memo[j]:
                    continue
                memo[j] = i

        count_ = 1
        div = i
        while div > 1:
            div //= memo[div]
            count_ += 1
        ans[i] = count_


n = int(input())

ans = [0] * (n + 1)
ans[1] = 1

Sieve(n)

print(*ans[1:])