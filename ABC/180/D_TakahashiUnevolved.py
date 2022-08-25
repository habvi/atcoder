X, Y, A, B = map(int, input().split())

x = X
ans = 0
while x * A < min(Y, X + B):
    x *= A
    ans += 1

ans += (Y - 1 - x) // B
print(ans)