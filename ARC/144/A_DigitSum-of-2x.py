n = int(input())

ans = ""
if n % 4:
    ans += str(n % 4)
ans += '4' * (n // 4)

print(n * 2)
print(ans)