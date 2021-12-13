n = int(input())
a = list(map(int, input().split()))
x = 0
for i in a:
    x ^= i

ans = [x ^ i for i in a]
print(*ans)