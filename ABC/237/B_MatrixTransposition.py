h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

for a in zip(*A):
    print(*a)