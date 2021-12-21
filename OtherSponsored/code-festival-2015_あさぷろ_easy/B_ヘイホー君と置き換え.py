n = int(input())
if n % 2 == 1:
    print(-1)
    exit()

s = input()
ans = 0
for i in range(n // 2):
    if s[i] != s[n//2 + i]:
        ans += 1
print(ans)