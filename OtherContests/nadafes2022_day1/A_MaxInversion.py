n = int(input())

ans = (n - 1) * n // 2
if n % 2:
    ans -= 1
print(ans)