X, Y, Z = map(int, input().split())

if 0 < Y < X:
    if Y < Z:
        print(-1)
        exit()
    ans = X
    if Z < 0:
        ans += abs(Z) * 2
elif X < Y < 0:
    if Z < Y:
        print(-1)
        exit()
    ans = -X
    if Z >= 0:
        ans += Z * 2
else:
    ans = abs(X)
print(ans)