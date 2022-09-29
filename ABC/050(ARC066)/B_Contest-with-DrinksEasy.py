N = int(input())
T = list(map(int, input().split()))
M = int(input())

total = sum(T)
for _ in range(M):
    p, x = map(int, input().split())
    p -= 1
    print(total - T[p] + x)