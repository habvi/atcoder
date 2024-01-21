N = int(input())

total_x = 0
total_y = 0
for _ in range(N):
    x, y = map(int, input().split())
    total_x += x
    total_y += y

if total_x == total_y:
    print("Draw")
elif total_x > total_y:
    print("Takahashi")
else:
    print("Aoki")