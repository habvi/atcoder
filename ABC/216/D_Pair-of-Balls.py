from collections import defaultdict

n, m = map(int, input().split())

balls = []
for _ in range(m):
    _ = int(input())
    A = list(map(int, input().split()))
    balls.append(A[::-1])

selected = defaultdict(lambda : -1)
que = list(range(m))
while que:
    i = que.pop()
    ball = balls[i].pop()

    if selected[ball] == -1:
        selected[ball] = i
    else:
        if balls[i]:
            que.append(i)
        j = selected[ball]
        if balls[j]:
            que.append(j)
        del selected[ball]

print('Yes' if not selected else 'No')