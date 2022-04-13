n = int(input())
A = list(map(int, input().split()))

if (total := sum(A)) % n:
    print(-1)
    exit()

each = total // n

now, num = 0, 0
ans = 0
for a in A:
    now += a
    num += 1
    if now == each * num:
        ans += (num - 1)
        now, num = 0, 0
print(ans)