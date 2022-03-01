n = int(input())
T = list(map(int, input().split()))
m = int(input())
sm = sum(T)
for _ in range(m):
    p, x = map(int, input().split())
    p -= 1
    print(sm - T[p] + x)