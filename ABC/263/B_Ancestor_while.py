N = int(input())
P = list(map(int, input().split()))

ans = 1
a = P[-1]
while a != 1:
    ans += 1
    a = P[a - 2]
print(ans)