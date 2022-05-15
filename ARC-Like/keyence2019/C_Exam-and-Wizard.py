n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
minus = []
ans = 0
for a, b in zip(A, B):
    if a < b:
        res += b - a
        ans += 1
    elif a > b:
        minus.append(a - b)

minus.sort()
while res > 0 and minus:
    res -= minus.pop()
    ans += 1

print(ans if res <= 0 else -1)