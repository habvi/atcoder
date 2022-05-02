from collections import defaultdict

n, m = map(int, input().split())

balls = []
for _ in range(m):
    k = int(input())
    A = list(map(int, input().split()))
    balls.append(A[::-1])

selected = defaultdict(lambda : -1)

check = list(range(m))
while check:
    i = check.pop()
    ball = balls[i].pop()

    if selected[ball] == -1:
        selected[ball] = i
    else:
        if balls[i]:
            check.append(i)
        j = selected[ball]
        if balls[j]:
            check.append(j)
        del selected[ball]

print('Yes' if not selected else 'No')