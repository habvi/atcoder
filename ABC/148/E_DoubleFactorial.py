n = int(input())
if n % 2:
    print(0)
    exit()

x = 10
ans = 0
while n // x > 0:
    ans += n // x
    x *= 5
print(ans)