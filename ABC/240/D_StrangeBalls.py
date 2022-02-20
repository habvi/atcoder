from collections import deque

n = int(input())
A = list(map(int, input().split()))

kind = [(-1, -1)]
q = deque([])

for a in A:
    num, count_ = kind[-1]
    if num != a:
        kind.append((a, 1))
        q.append(a)
        ans = len(q)
    else:
        if count_ + 1 == a:
            kind.pop()
            for _ in range(count_):
                q.pop()
        else:
            kind.pop()
            kind.append((a, count_ + 1))
            q.append(a)
        ans = len(q)

    print(ans)