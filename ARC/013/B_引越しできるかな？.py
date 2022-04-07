n = int(input())

box = []
for _ in range(n):
    box.append(sorted(map(int, input().split())))

ans = 1
for size in zip(*box):
    ans *= max(size)
print(ans)