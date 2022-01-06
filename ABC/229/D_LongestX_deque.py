from collections import deque
S = input()
k = int(input())
q = deque([])
ld, lx = 0, 0
ans = 0
for s in S:
    if s == "X":
        lx += 1
        q.append(s)
        ans = max(ans, len(q))
        continue

    while q and ld >= k:
        rm = q.popleft()
        if rm == ".":
            ld -= 1
        else:
            lx -= 1

    if k != 0:
        ld += 1
        q.append(s)
        ans = max(ans, len(q))
print(ans)