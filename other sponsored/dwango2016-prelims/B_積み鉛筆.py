n = int(input())
k = list(map(int, input().split()))
a = []
for i in range(n - 2):
    a.append(min(k[i], k[i + 1]))

ans = [k[0]] + a + [k[-1]]
print(*ans)