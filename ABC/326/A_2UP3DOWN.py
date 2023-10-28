X, Y = map(int, input().split())

print("Yes" if 0 <= Y - X <= 2 or 0 <= X - Y <= 3 else "No")