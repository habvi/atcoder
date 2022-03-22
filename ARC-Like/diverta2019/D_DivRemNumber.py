n = int(input())

ans = 0
i = 1
while i * i <= n:
    if n % i == 0:
        j = n // i - 1
        if j > 0 and n // j == n % j:
            ans += j
    i += 1

print(i, ans)