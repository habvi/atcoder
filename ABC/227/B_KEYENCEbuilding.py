n = int(input())
A = list(map(int, input().split()))

s = set()
for i in range(1, 1001):
    for j in range(1, 1001):
        s.add(4*i*j + 3*i + 3*j)

ans = 0
for a in A:
    ans += a not in s
print(ans)