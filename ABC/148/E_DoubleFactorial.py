n = int(input())

if n % 2:
    print(0)
    exit()

k = 10
ans = 0
while k <= n:
    ans += n // k
    k *= 5

print(ans)