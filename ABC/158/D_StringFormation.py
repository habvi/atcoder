from collections import deque

S = input()
Q = int(input())

d = deque(list(S))
rev = 0
for _ in range(Q):
    t, *fc = input().split()
    if t == '1':
        rev = 1 - rev
    else:
        f, c = fc
        if (not rev and f == '1') or (rev and f == '2'):
            d.appendleft(c)
        else:
            d.append(c)
ans = ''.join(d)
print(ans[::-1] if rev else ans)