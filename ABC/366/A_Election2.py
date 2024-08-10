N, T, A = map(int, input().split())

border = N // 2 + 1
print("Yes" if T >= border or A >= border else "No")
