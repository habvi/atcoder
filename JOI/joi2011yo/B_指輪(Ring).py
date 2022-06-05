target = input()
n = int(input())

ans = 0
for _ in range(n):
    S = input()
    S *= 2
    ans += (target in S)
print(ans)