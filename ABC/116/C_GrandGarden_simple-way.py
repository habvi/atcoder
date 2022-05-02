n = int(input())
H = list(map(int, input().split()))

ans = 0
pre = 0
for h in H:
    ans += max(0, h - pre)
    pre = h
print(ans)



# -----------------------------------
n = int(input())
H = [0, *map(int, input().split()), 0]

ans = 0
for i in range(n + 1):
    ans += abs(H[i] - H[i + 1])
print(ans // 2)