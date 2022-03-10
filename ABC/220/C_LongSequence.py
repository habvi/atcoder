n = int(input())
A = list(map(int, input().split()))
X = int(input())

total = sum(A)
ans, res = divmod(X, total)
ans *= n

for a in A:
    res -= a
    ans += 1
    if res < 0:
        break
print(ans)